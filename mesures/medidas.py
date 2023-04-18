# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MEDIDAS_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class MEDIDAS(object):
    def __init__(self, data, period=2, distributor=None, file_type='medidas_cnmc', compression='bz2', by_upr=False,
                 version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param file_type: str in ('medidas_cnmc', 'medidas_ree')
        :param compression: 'bz2', 'gz'... OR False otherwise
        :param by_upr: boolean
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file_type = file_type
        self.by_upr = by_upr
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'medidas'
        self.version = version
        self.period = period
        self.distributor = distributor
        self.default_compression = compression
        self.columns = columns

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
        filename = "{prefix}_{distributor}_{measures_date}_{period}_{timestamp}.{version}".format(
            prefix=self.prefix,
            distributor=self.distributor,
            measures_date=self.measures_date,
            period=self.period,
            timestamp=self.generation_date.strftime('%Y%m%d'),
            version=self.version
        )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    def filename_by_upr(self, upr):
        filename = "{prefix}_{distributor}_{upr}_{measures_date}_{period}_{timestamp}.{version}".format(
            prefix=self.prefix,
            distributor=self.distributor,
            upr=upr,
            measures_date=self.measures_date,
            period=self.period,
            timestamp=self.generation_date.strftime('%Y%m%d'),
            version=self.version
        )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def cnmc_filename(self):
        filename = "{prefix}_{distributor}_{cil}_{measures_date}_{period}_{timestamp}.txt".format(
            prefix=self.prefix,
            distributor=self.distributor,
            cil=self.cil,
            measures_date=self.measures_date,
            period=self.period,
            timestamp=self.generation_date.strftime('%Y%m%d')
        )

        return filename

    def cnmc_filename_by_upr(self, upr):
        filename = "{prefix}_{distributor}_{upr}_{measures_date}_{period}_{timestamp}.txt".format(
            prefix=self.prefix,
            distributor=self.distributor,
            upr=upr,
            measures_date=self.measures_date,
            period=self.period,
            timestamp=self.generation_date.strftime('%Y%m%d')
        )

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{period}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date,
            period=self.period, timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    @property
    def r2(self):
        return int(self.file['r2'].sum())

    @property
    def r3(self):
        return int(self.file['r3'].sum())

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def hours_per_cil(self):
        return self.file['cil'].value_counts().reset_index().to_dict('records')

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
            df['timestamp'] = df.apply(lambda row: row['timestamp'].strftime(DATETIME_MASK), axis=1)
        except Exception as err:
            # Timestamp is already well parsed
            pass

        # Group by CIL and balance energies
        group_fields = ['cil', 'timestamp', 'season']

        if self.by_upr:
            group_fields.append('uprs')

        df = df.groupby(
            group_fields
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
            balance = ae_m - ai_m
            df.at[idx, 'ae'] = balance
            # REE file does not admit negative balance
            if self.file_type == 'medidas_ree':
                df.at[idx, 'ae'] = max(0, balance)

        for key in ['power_factor', 'power_factor_type']:
            if key not in df:
                df[key] = ''
            df[key] = df[key].astype('str')

        return df

    def writer(self):
        """
        MEDIDAS contains hourly generation curves
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        measures_date = datetime.strptime(daymin, DATETIME_MASK)
        self.measures_date = measures_date.strftime('%Y%m')

        cil = self.file['cil'].min()
        self.cil = cil

        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  check_line_terminator_param(): ';\n'
                  }

        if self.file_type == 'medidas_cnmc':
            if self.by_upr:
                zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
                uprs = list(self.file['uprs'].unique())
                for upr in uprs:
                    df = self.file[self.file['uprs'] == upr]
                    file_path = os.path.join('/tmp', self.cnmc_filename_by_upr(upr))
                    df.to_csv(file_path, **kwargs)
                    zipped_file.write(file_path, arcname=os.path.basename(file_path))
                zipped_file.close()
                file_path = zipped_file.filename
            else:
                file_path = os.path.join('/tmp', self.cnmc_filename)
                self.file.to_csv(file_path, **kwargs)
                zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
                zipped_file.write(file_path, arcname=os.path.basename(file_path))
                zipped_file.close()
                file_path = zipped_file.filename
        else:
            if self.by_upr:
                zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
                uprs = list(self.file['uprs'].unique())
                for upr in uprs:
                    df = self.file[self.file['uprs'] == upr]
                    file_path = os.path.join('/tmp', self.filename_by_upr(upr))
                    df.to_csv(file_path, **kwargs)
                    zipped_file.write(file_path, arcname=os.path.basename(file_path))
                zipped_file.close()
                file_path = zipped_file.filename
            else:
                file_path = os.path.join('/tmp', self.filename)
                kwargs.update({'compression': self.default_compression})
                self.file.to_csv(file_path, **kwargs)
        return file_path
