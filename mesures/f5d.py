# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.f5 import F5, DTYPES
import os
import pandas as pd

TYPES = DTYPES.copy()
TYPES.update({'factura': 'category'})


class F5D(F5):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', columns=COLUMNS, dtypes=TYPES):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(F5D, self).__init__(data, distributor=distributor, comer=comer, compression=compression,
                                  columns=columns, dtypes=dtypes)
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

    def cut_by_dates(self, di, df):
        """
        Cut File by dates, discard > and <
        :param di: str datetime LIKE 2021-01-01 01:00
        :param df: str datetime LIKE 2021-02-01 00:00
        """
        self.file = self.file[(self.file.timestamp >= di) & (self.file.timestamp <= df)]

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns, dtype=self.dtypes)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        if 'firmeza' not in df:
            df['firmeza'] = df['method'].apply(lambda x: 1 if x in (1, 3) else 0)

        if 'factura' not in df:
            df['factura'] = 'F0000000000'

        df = df.groupby(['cups', 'timestamp', 'season', 'firmeza', 'method', 'factura']).aggregate(
            {'ai': 'sum', 'ae': 'sum', 'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        ).reset_index()

        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))

        for key in ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')
        df = df[self.columns]
        return df

    def writer(self):
        """
        :return: file path of generated F5D File
        """
        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  'line_terminator': ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
