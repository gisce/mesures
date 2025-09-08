# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.base import BaseStream
from mesures.f5 import F5, DTYPES
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd

TYPES = DTYPES.copy()
TYPES.update({'factura': 'category'})
ENERGY_MAGNS = ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']
CNMC_ENERGY_MAGNS = ['ai_fix', 'ae_fix']

class F5D(F5):
    def __init__(self, data, file_format='REE', distributor=None, comer=None, compression='bz2', columns=COLUMNS, dtypes=TYPES, version=0, skip_reader=False):
        """
        :param data: list of dicts or absolute file_path
        :param file_format: str format to generate
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """

        self.file_format = file_format
        if self.file_format == 'CNMC':
            columns = columns + CNMC_ENERGY_MAGNS
        self.columns = columns

        super(F5D, self).__init__(data, distributor=distributor, comer=comer, compression=compression,
                                  columns=columns, dtypes=dtypes, version=version, skip_reader=skip_reader)
        self.prefix = 'F5D'


    @property
    def filename(self):
        filename = "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
        )
        if self.default_compression:
            filename += ".{compression}".format(compression=self.default_compression)
        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK)
        )

    @property
    def ai_fix(self):
        if not self.file_format == 'CNMC':
            res = 0
        else:
            res = int(self.file['ai_fix'].sum())
        return res

    @property
    def ae_fix(self):
        if not self.file_format == 'CNMC':
            res = 0
        else:
            res = int(self.file['ae_fix'].sum())
        return res

    def cut_by_dates(self, di, df):
        """
        Cut File by dates, discard > and <
        :param di: str datetime LIKE 2021-01-01 01:00
        :param df: str datetime LIKE 2021-02-01 00:00
        """
        self.file = self.file[(self.file.timestamp >= di) & (self.file.timestamp <= df)]

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns + ['res'], dtype=self.dtypes)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        if 'firmeza' not in df:
            df['firmeza'] = df['method'].apply(lambda x: 1 if x in (1, 3) else 0)

        if 'factura' not in df:
            df['factura'] = 'F0000000000'

        agregates = {'ai': 'sum', 'ae': 'sum', 'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        if self.file_format == 'CNMC':
            agregates.update({'ai_fix': 'sum', 'ae_fix': 'sum'})

        df = df.groupby(['cups', 'timestamp', 'season', 'firmeza', 'method', 'factura']).aggregate(
            agregates).reset_index()

        if isinstance(filepath, list):
            df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))

        magnituds = ENERGY_MAGNS
        if self.file_format == 'CNMC':
            magnituds += CNMC_ENERGY_MAGNS

        for key in magnituds:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')
        df = df[self.columns]
        return df

    def writer(self):
        """
        :return: file path of generated F5D File
        """
        existing_files = os.listdir('/tmp')
        if existing_files and self.default_compression != 'zip':
            versions = [int(f.split('.')[1]) for f in existing_files if self.filename.split('.')[0] in f and '.zip' not in f]
            if versions:
                self.version = max(versions) + 1

        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  check_line_terminator_param(): ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        if kwargs.get('compression', False) == 'zip':
            self.default_compression = False
            zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
            file_path = os.path.join('/tmp', self.filename)
            kwargs.pop('compression')
            self.file.to_csv(file_path, **kwargs)
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
            file_path = zipped_file.filename
        else:
            self.file.to_csv(file_path, **kwargs)
        return file_path


class F5DStream(BaseStream, F5D):
    """Streaming replacement for :class:`mesures.f5d.F5D`."""

    _GROUP = ['cups', 'timestamp', 'season', 'firmeza', 'method', 'factura']
    _ENERGY_BASE = list(ENERGY_MAGNS)
    _SORT = ['timestamp', 'factura', 'cups']

    def __init__(self, distributor=None, comer=None, file_format='REE',
                 compression='bz2', columns=COLUMNS, version=0):
        if F5D is None:
            raise RuntimeError("The 'mesures' library is not installed")

        self._ENERGY = list(self._ENERGY_BASE)
        if file_format == 'CNMC':
            self._ENERGY += CNMC_ENERGY_MAGNS

        # cols = self._GROUP + self._ENERGY
        dtype_map = TYPES
        for col in self._ENERGY:
            dtype_map.setdefault(col, 'int32')

        aggregation_map = {col: 'sum' for col in self._ENERGY}

        F5D.__init__(self, data=[], file_format=file_format,
                      distributor=distributor, comer=comer,
                      compression=compression, columns=columns,
                      dtypes=dtype_map, version=version, skip_reader=True)

        BaseStream.__init__(self, selection_columns=columns,
                            aggregation_columns=self._GROUP,
                            aggregation_map=aggregation_map,
                            sort_columns=self._SORT,
                            dtype_map=dtype_map)

        self.prefix = 'F5D'
        self.generation_date = datetime.now()
        self.file_format = file_format

    def add_chunk(self, chunk):
        for d in chunk:  # ensure 'factura' present
            d.setdefault('factura', 'F0000000000')
        return super(F5DStream, self).add_chunk(chunk)

    def writer(self):
        df = self.data_frame
        tmp_f5d = F5D(df.to_dict('records'), file_format=self.file_format,
                       distributor=self.distributor, comer=self.comer,
                       compression=self.default_compression, columns=self.columns,
                       dtypes=self.dtypes, version=self.version)
        return tmp_f5d.writer()

    def __exit__(self, exc_type, _exc, _tb):
        if exc_type is None and len(self._agg):
            self.writer()
