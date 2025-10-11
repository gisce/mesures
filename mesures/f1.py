# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F1_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd
import numpy as np


class F1(object):
    def __init__(self, data, distributor=None, compression='bz2', allow_decimals=False, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = COLUMNS
        self.allow_decimals = allow_decimals
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'F1'
        self.version = version
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
        filename = '{prefix}_{distributor}_{measures_date}_{timestamp}.{version}'.format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date[:10].replace('/', ''),
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
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

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['tipo_medida'] = 11

        if 'firmeza' not in df:
            df['firmeza'] = np.where(
                df['method'].isin([1,3]),
                1,
                0
            )

        df = df.groupby(
            ['cups', 'tipo_medida', 'timestamp', 'season', 'method', 'firmeza']
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

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_MASK)

        df['res'] = 0
        df['res2'] = 0

        if not self.allow_decimals:
            for key in ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']:
                df[key] = df[key].astype('int')

        df = df[self.columns]
        return df

    def writer(self):
        """
        F1 contains a curve files diary on zip
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin

        existing_files = os.listdir('/tmp')
        if existing_files:
            zip_versions = [int(f.split('.')[1])
                            for f in existing_files if self.zip_filename.split('.')[0] in f and '.zip' in f]
            if zip_versions:
                self.version = max(zip_versions) + 1

        zip_measures_date = self.measures_date
        zip_version = self.version
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = (datetime.strptime(daymin, DATETIME_MASK) + timedelta(days=1)).strftime(DATETIME_MASK)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            # Avoid to generate file if dataframe is empty
            if len(dataf):
                existing_files = os.listdir('/tmp')
                if existing_files:
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
                dataf.to_csv(file_path, **kwargs)
                zipped_file.write(file_path, arcname=os.path.basename(file_path))

            daymin = df
        zipped_file.close()
        self.measures_date = zip_measures_date
        self.version = zip_version
        return zipped_file.filename
