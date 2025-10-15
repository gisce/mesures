# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MCIL345_HEADER as COLUMNS
from mesures.mcil345 import MCIL345
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class MCIL345QH(MCIL345):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(MCIL345QH, self).__init__(data, distributor=distributor, compression=compression, version=version)
        self.prefix = 'MCIL345QH'

    def reader(self, filepath):
        """Overrided to use DATETIME_HOUR_MASK instead of DATE_MASK"""
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_HOUR_MASK)
        except Exception as err:
            # Timestamp is already well parsed
            pass

        # Group by CIL and balance energies
        df = df.groupby(
            ['cil', 'timestamp', 'season']
        ).agg(
            {'ai': 'sum',
             'ae': 'sum',
             'r1': 'sum',
             'r2': 'sum',
             'r3': 'sum',
             'r4': 'sum',
             'read_type': 'min'}
        ).reset_index()

        df = df.sort_values(['cil', 'timestamp', 'season'])

        for idx, row in df.iterrows():
            ai_m = row.get('ai', 0.0)
            ae_m = row.get('ae', 0.0)
            if ai_m >= ae_m:
                df.at[idx, 'ai'] = ai_m - ae_m
                df.at[idx, 'ae'] = 0.0
            else:
                df.at[idx, 'ai'] = 0.0
                df.at[idx, 'ae'] = ae_m - ai_m

        return df

    def writer(self):
        """
        MCIL345QH contains hourly generation curves
        Overrided to use DATETIME_HOUR_MASK instead of DATE_MASK
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