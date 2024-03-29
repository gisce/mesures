# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import A5D_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
import os
import pandas as pd


class A5D(object):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'A5D'
        self.default_compression = compression
        self.version = version
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
            return "{prefix}_{distributor}_{comer}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    @property
    def total(self):
        return int(self.file['ai'].sum())

    @property
    def ai(self):
        return int(self.file['ai'].sum())

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=self.columns
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df = df.groupby(['cups', 'timestamp', 'season', 'factura']).aggregate(
            {'ai': 'sum', 'ae': 'sum',
             'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        ).reset_index()
        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
        for key in ['r1', 'r2', 'r3', 'r4', 'ae', 'method', 'firmeza']:
            df[key] = ''
        df = df[self.columns]
        return df

    def writer(self):
        """
        A5D contains a hourly raw curve
        :return: file path
        """
        existing_files = os.listdir('/tmp')
        if existing_files:
            versions = [int(f.split('.')[1]) for f in existing_files if self.filename.split('.')[0] in f]
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

        self.file.to_csv(file_path, **kwargs)
        return file_path
