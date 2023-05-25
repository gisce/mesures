# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.f1 import F1
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class F1QH(F1):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(F1QH, self).__init__(data=data, distributor=distributor, compression=compression, version=version)
        self.prefix = 'F1QH'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=self.columns
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['tipo_medida'] = 11

        if 'firmeza' not in df:
            df['firmeza'] = df['method'].apply(lambda x: 1 if x in (1, 3) else 0)

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

        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime(DATETIME_HOUR_MASK))

        df['res'] = 0
        df['res2'] = 0
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
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = (datetime.strptime(daymin, DATETIME_HOUR_MASK) + timedelta(days=1)).strftime(DATETIME_HOUR_MASK)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            # dataf['timestamp'] = dataf['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
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
            daymin = df
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
        zipped_file.close()
        return zipped_file.filename
