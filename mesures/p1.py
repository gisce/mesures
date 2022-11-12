# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import P1_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from zipfile import ZipFile
import os
import pandas as pd


class P1(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = columns
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'P1'
        self.version = 0
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
        filename = "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                measures_date=self.measures_date[:10].replace('/', ''),
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )
        if self.default_compression:
            filename += ".{compression}".format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor,
            measures_date=self.measures_date[:10].replace('/', ''),
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK)
        )

    @property
    def total(self):
        return float(self.file['ai'].sum())

    @property
    def ai(self):
        return float(self.file['ai'].sum())

    @property
    def ae(self):
        return float(self.file['ae'].sum())

    @property
    def r1(self):
        return float(self.file['r1'].sum())

    @property
    def r2(self):
        return float(self.file['r2'].sum())

    @property
    def r3(self):
        return float(self.file['r3'].sum())

    @property
    def r4(self):
        return float(self.file['r4'].sum())

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['tipo_medida'] = 11
        df.groupby(['cups', 'tipo_medida', 'timestamp', 'season', 'method']).aggregate({'ai': 'sum'})

        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime(DATETIME_MASK))

        df['method'] = 1
        df['firmeza'] = 1
        df['res'] = 0
        df['res2'] = 0

        for key in self.columns:
            if 'quality' in key and key not in df:
                df[key] = 0
        df = df[self.columns]
        return df

    def writer(self):
        """
        P1 contains a curve files diary on zip
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
            file_path = os.path.join('/tmp', self.filename)
            kwargs = {'sep': ';',
                      'header': False,
                      'columns': self.columns,
                      'index': False,
                      'line_terminator': ';\n'
                      }
            if self.default_compression:
                kwargs.update({'compression': self.default_compression})

            dataf.to_csv(file_path, **kwargs)
            daymin = df
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
        zipped_file.close()
        return zipped_file.filename
