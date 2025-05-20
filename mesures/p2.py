# -*- coding: utf-8 -*-
from mesures.headers import P2_HEADER as COLUMNS
from mesures.p1 import P1
from mesures.dates import *
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os


class P2(P1):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P2, self).__init__(data, distributor, compression=compression, columns=columns, version=version)
        self.prefix = 'P2'

    def writer(self):
        """
        P2D contains all curve measure in one file
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = (datetime.strptime(daymin, DATETIME_MASK) + timedelta(days=1)).strftime(DATETIME_MASK)
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