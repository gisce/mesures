# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MCIL345_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class MCIL345(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'MCIL345'
        self.version = version
        self.distributor = distributor
        self.default_compression = compression
        self.measures_date = None

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
        filename = "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
            prefix=self.prefix,
            distributor=self.distributor,
            measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
            version=self.version
            )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}.zip".format(
            prefix=self.prefix,
            distributor=self.distributor,
            measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
            version=self.version
        )

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    @property
    def ai(self):
        return int(self.file['ai'].sum())

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
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")
        try:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['timestamp'] = df['timestamp'].dt.strftime(DATE_MASK)
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
        MCIL345 contains hourly generation curves
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
            df = (datetime.strptime(daymin, DATE_MASK) + timedelta(days=1)).strftime(DATE_MASK)
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
