# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MCIL345_HEADER as COLUMNS
from mesures.mcil345 import MCIL345
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class MCIL345QH(MCIL345):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(MCIL345QH, self).__init__(data, distributor=distributor, compression=compression, version=version)
        self.prefix = 'MCIL345QH'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=COLUMNS)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")
        try:
            df['timestamp'] = df.apply(lambda row: row['timestamp'].strftime(DATETIME_HOUR_MASK), axis=1)
        except Exception as err:
            # Timestamp is already well parsed
            pass

        # Group by CIL and balance energies
        df = df.groupby(
            ['cil',
             'timestamp',
             'season']
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
        MCIL345 contains hourly generation curves
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = (datetime.strptime(daymin, DATETIME_HOUR_MASK) + timedelta(days=1)).strftime(DATETIME_HOUR_MASK)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            # dataf['timestamp'] = dataf['timestamp'].apply(lambda x: x.strftime(DATETIME_HOUR_MASK))
            # Avoid to generate file if dataframe is empty
            if len(dataf):
                existing_files = os.listdir('/tmp')
                if existing_files:
                    versions = [int(f.split('.')[1]) for f in existing_files if self.zip_filename.split('.')[0] in f]
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
        return zipped_file.filename