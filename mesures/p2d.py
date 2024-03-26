# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import P2_HEADER as COLUMNS
from mesures.p2 import P2
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class P2D(P2):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P2D, self).__init__(data, distributor, compression=compression, columns=columns, version=version)
        self.prefix = 'P2D'
        self.comer = comer
        self.measures_date = None

    @property
    def filename(self):
        filename = "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.{version}.zip".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
            version=self.version
        )

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

        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime(DATETIME_MASK))

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
                df[key] = 0
        df = df[self.columns]
        return df

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
