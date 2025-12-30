# -*- coding: utf-8 -*-
from mesures.headers import P2_HEADER as COLUMNS
from mesures.p1 import P1
from mesures.dates import *
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class P2(P1):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P2, self).__init__(data, distributor, compression=compression, columns=columns, version=version)
        self.prefix = 'P2'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['tipo_medida'] = 11

        df.groupby(
            ['cups', 'tipo_medida', 'timestamp', 'season', 'method']
        ).aggregate(
            {'ai': 'sum',
             'ae': 'sum',
             'r1': 'sum',
             'r2': 'sum',
             'r3': 'sum',
             'r4': 'sum'}
        )

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_MASK)

        df['method'] = 1
        df['res'] = 0
        df['res2'] = 0

        df['ai'] = df['ai'].astype('int')
        df['ae'] = df['ae'].astype('int')
        df['r1'] = df['r1'].astype('int')
        df['r2'] = df['r2'].astype('int')
        df['r3'] = df['r3'].astype('int')
        df['r4'] = df['r4'].astype('int')

        for key in self.columns:
            if 'quality' in key and key not in df:
                df[key] = '0'

        df = df[self.columns]
        return df

    def writer(self):
        """
        P2 contains all curve measure in one file
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