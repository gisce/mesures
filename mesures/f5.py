# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F5D_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
from zipfile import ZipFile
import os
import pandas as pd


DTYPES = {'cups': 'category',
          'season': 'category',
          'ai': 'int64',
          'ae': 'int64',
          'r1': 'int64',
          'r2': 'int64',
          'r3':  'int64',
          'r4': 'int64',
          'method': 'category',
          'firmeza': 'category',
          'factura': 'category',
          'res': 'category'}


class F5(object):
    def __init__(self, data, distributor=None, comer=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'F5'
        self.default_compression = compression
        self.version = 0
        self.distributor = distributor
        self.comer = comer

    def __repr__(self):
        return "{}: {} Wh".format(self.filename, self.total)

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        if self.default_compression:
            return "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                measures_date=self.measures_date.strftime('%Y%m%d'), timestamp=self.generation_date.strftime('%Y%m%d'),
                version=self.version, compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                measures_date=self.measures_date.strftime('%Y%m%d'), timestamp=self.generation_date.strftime('%Y%m%d'),
                version=self.version
            )

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            measures_date=self.measures_date.strftime('%Y%m%d'), timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def total(self):
        return int(self.file['ai'].sum())

    @property
    def ai(self):
        return int(self.file['ai'].sum())

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    @property
    def r1(self):
        return int(self.file['r1'].sum())

    @property
    def r2(self):
        return int(self.file['r2'].sum())

    @property
    def r3(self):
        return int(self.file['r3'].sum())

    @property
    def r4(self):
        return int(self.file['r4'].sum())

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    @property
    def number_of_invoices(self):
        return len(list(set(self.file['factura'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=columns + ['res'],
                dtype=DTYPES
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        if 'firmeza' not in df:
            df['firmeza'] = df['method'].apply(lambda x: 1 if x in (1, 3) else 0)
        if 'factura' not in df:
            df['factura'] = 'F0000000000'
        for key in ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')
        df = df[columns]
        return df

    def writer(self):
        """
        F5 contains a curve files diary on zip
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        #todo: get a zip filename without measures_date
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            dataf['timestamp'] = dataf['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
            file_path = os.path.join('/tmp', self.filename)
            kwargs = {'sep': ';',
                      'header': False,
                      'columns': columns,
                      'index': False,
                      'line_terminator': ';\n'
                      }
            if self.default_compression:
                kwargs.update({'compression': self.default_compression})

            dataf.to_csv(file_path, **kwargs)
            daymin = df
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
        zipped_file.close()
        return zipped_file.filename
