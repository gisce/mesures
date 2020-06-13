import os
import pandas as pd
from zipfile import ZipFile
from configparser import ConfigParser
from datetime import datetime, timedelta
from mesures.headers import F1_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve

class F1(object):
    def __init__(self, data, distributor=None):
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'F1'
        self.version = 0
        self.distributor = distributor

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
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m%d'),
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    @property
    def simple_filename(self):
        return "{prefix}_{distributor}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def total(self):
        return self.file['ai'].sum()

    @property
    def ai(self):
        return self.file['ai'].sum()

    @property
    def ae(self):
        return self.file['ae'].sum()

    @property
    def r1(self):
        return self.file['r1'].sum()

    @property
    def r2(self):
        return self.file['r2'].sum()

    @property
    def r3(self):
        return self.file['r3'].sum()

    @property
    def r4(self):
        return self.file['r4'].sum()

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            return pd.read_csv(
                filepath, sep=';', names=columns
            )
        if isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
            df['tipo_medida'] = 11
            df = df.groupby(
                [
                    'cups', 'tipo_medida', 'timestamp', 'season'
                ]
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
            df['method'] = 1
            df['firmeza'] = 1
            df['res'] = 0
            df['res2'] = 0
            df = df[columns]
            return df

    def writer(self):
        """
        F1 contains a curve files diary on zip
        :return: file path
        """
        zipped_file = ZipFile(os.path.join('/tmp', self.simple_filename), 'w')
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        while daymin <= daymax:
            di = daymin
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            filepath = os.path.join('/tmp', self.filename)
            dataf.to_csv(
                filepath, sep=';', header=False, columns=columns, index=False, line_terminator=';\n'
            )
            daymin = df
            zipped_file.write(filepath)
        zipped_file.close()
        return zipped_file.filename
