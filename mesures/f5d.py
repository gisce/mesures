# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F5D_HEADER as COLUMNS
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
    def __init__(self, data, file_format='REE', distributor=None, comer=None, compression='bz2',
                 columns=COLUMNS, dtypes=TYPES, version=0):
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
                                  columns=columns, dtypes=dtypes, version=version)
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
            df['firmeza'] = np.where(
                df['method'].isin([1, 3]),
                1,
                0
            )

        if 'factura' not in df:
            df['factura'] = 'F0000000000'

        agregates = {'ai': 'sum', 'ae': 'sum', 'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        if self.file_format == 'CNMC':
            agregates.update({'ai_fix': 'sum', 'ae_fix': 'sum'})

        df = df.groupby(
            ['cups', 'timestamp', 'season', 'firmeza', 'method', 'factura']
        ).aggregate(
            agregates
        ).reset_index()

        if isinstance(filepath, list):
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_HOUR_MASK)

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
            versions = [int(f.split('.')[1])
                        for f in existing_files if self.filename.split('.')[0] in f and '.zip' not in f]
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
