# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.f1 import F1
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd
import numpy as np


class F1QH(F1):
    def __init__(self, data, distributor=None, compression='bz2', allow_decimals=False, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(F1QH, self).__init__(data=data, distributor=distributor, compression=compression,
                                   allow_decimals=allow_decimals, version=version)
        self.prefix = 'F1QH'

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
                df['method'].isin([1, 3]),
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
        df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_HOUR_MASK)

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
            df = (datetime.strptime(daymin, DATETIME_HOUR_MASK) + timedelta(days=1)).strftime(DATETIME_HOUR_MASK)
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
