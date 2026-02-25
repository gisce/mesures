# -*- coding: utf-8 -*-
from mesures.dates import DATETIME_HOUR_MASK, timedelta
from mesures.pmest import PMEST
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os


class PMESTQH(PMEST):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(PMESTQH, self).__init__(data, distributor, compression=compression, version=version)
        self.prefix = 'PMESTQH'

    def writer(self):
        """
        PMEST contains a curve files diary on zip
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
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            # Avoid to generate file if dataframe is empty
            if len(dataf):
                dataf['timestamp'] = dataf['timestamp'].dt.strftime(DATETIME_HOUR_MASK)
                dataf['timestamp'] = dataf['timestamp'].astype(str)
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