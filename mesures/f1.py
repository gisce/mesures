import pandas as pd
from datetime import datetime
from mesures.headers import F1_HEADER
from mesures.curves.curve import DummyCurve
import os


class F1(object):
    def __init__(self, distributor, data):
        self.header = F1_HEADER
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.distributor = distributor
        self.generation_date = datetime.now()
        self.prefix = 'F1'
        self.version = 1

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
        return "{prefix}_{distributor}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, version=self.version
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
                filepath, sep=';', names=self.header
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
            df['firmeza'] = 0
            df['res'] = 0
            df['res2'] = 0
            df = df[F1_HEADER]
            return df

    def writer(self):
        filepath = os.path.join('/tmp', self.filename)
        self.file.to_csv(
            filepath, sep=';', header=False, columns=F1_HEADER, index=False, line_terminator=';\n'
        )
        return filepath

    def separe(self):
        self.file['day'] = self.file['datetime'].apply(lambda x: x[:10])
        daymin = min(list(set(self.file['day'])))
        daymax = max(list(set(self.file['day'])))
