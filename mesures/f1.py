# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F1_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class F1(object):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
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
        self.prefix = 'F1'
        self.version = version
        self.distributor = distributor
        self.default_compression = compression

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
        filename = '{prefix}_{distributor}_{measures_date}_{timestamp}.{version}'.format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date[:10].replace('/', ''),
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def total(self):
        return int(self.file['ai'].sum())

    @property
    def ai(self):
        return int(self.file['ai'].sum())

    @property
    def ae(self):
        return int(self.file['ae'].sum())

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
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

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

        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime(DATETIME_MASK))

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
            df = (datetime.strptime(daymin, DATETIME_MASK) + timedelta(days=1)).strftime(DATETIME_MASK)
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
