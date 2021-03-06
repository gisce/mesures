import os
import pandas as pd
from datetime import datetime, timedelta
from mesures.headers import P5D_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve

class P5D(object):
    def __init__(self, data, distributor=None, comer=None):
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'P5D'
        self.default_compression = 'bz2'
        self.version = 0
        self.distributor = distributor
        self.comer = comer

    def __repr__(self):
        return "{}: {} Wh".format(self.filename, self.total)

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
        return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
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
            df = df.groupby(['cups', 'timestamp', 'season']).aggregate({'ai': 'sum', 'ae': 'sum'}).reset_index()
            df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
            for key in ['ai', 'ae']:
                if key not in df:
                    df[key] = 0
                df[key] = df[key].astype('int32')
            df = df[columns]
            return df

    def writer(self):
        """
        P5D contains a hourly raw curve
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
