# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import PMEST_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
from zipfile import ZipFile
import os
import pandas as pd


class PMEST(object):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'PMEST'
        self.version = 0
        self.distributor = distributor
        self.default_compression = compression

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
            return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m%d'),
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m%d'),
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m%d'),
            timestamp=self.generation_date.strftime('%Y%m%d')
        )
    @property
    def total(self):
        return self.file['ai'].sum()

    @property
    def ai(self):
        return self.file['ai'].sum()

    @property
    def ae(self):
        return self.file['ae'].sum()

    @property
    def r1(self):
        return self.file['r1'].sum()

    @property
    def r2(self):
        return self.file['r2'].sum()

    @property
    def r3(self):
        return self.file['r3'].sum()

    @property
    def r4(self):
        return self.file['r4'].sum()

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=columns
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        if 'tipo_medida' not in df:
            # 8 absoluta
            # 11 incremental
            df['tipo_medida'] = 11
        if 'method' not in df:
            df['method'] = 7
        df = df.groupby(
            [
                'pm', 'tipo_medida', 'timestamp', 'season', 'method'
            ]
        ).aggregate(
            {
                'ai': 'sum',
                'ae': 'sum',
                'r1': 'sum',
                'r2': 'sum',
                'r3': 'sum',
                'r4': 'sum',
            }
        ).reset_index()
        df = df[columns]
        return df

    def writer(self):
        """
        PMEST contains a curve files diary on zip
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            dataf['timestamp'] = dataf.apply(lambda row: row['timestamp'].strftime('%Y/%m/%d %H'), axis=1)
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
