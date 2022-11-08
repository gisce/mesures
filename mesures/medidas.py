# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MEDIDAS_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
import os
import pandas as pd


class MEDIDAS(object):
    def __init__(self, data, period=2, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'medidas'
        self.version = 0
        self.period = period
        self.distributor = distributor
        self.default_compression = compression
        self.columns = columns

    def __repr__(self):
        return "{}: {} kWh".format(self.filename, self.total)

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
            return "{prefix}_{distributor}_{measures_date}_{period}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
                period=self.period, timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{measures_date}_{period}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
                period=self.period, timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{period}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
            period=self.period, timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    @property
    def r2(self):
        return int(self.file['r2'].sum())

    @property
    def r3(self):
        return int(self.file['r3'].sum())

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")
        try:
            df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M:%S'))
        except Exception as err:
            # Timestamp is already well parsed
            pass
        finally:
            df = df.groupby(
                ['cil', 'timestamp', 'season', 'power_factor', 'power_factor_type']
            ).aggregate(
                {'ae': 'sum', 'r2': 'sum', 'r3': 'sum', 'read_type': 'min'}
            ).reset_index()
            return df

    def writer(self):
        """
        MEDIDAS contains hourly generation curves
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        measures_date = datetime.strptime(daymin, '%Y/%m/%d %H:%M:%S')
        self.measures_date = measures_date
        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': columns,
                  'index': False,
                  'line_terminator': ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
