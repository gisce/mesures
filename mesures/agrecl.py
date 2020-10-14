import os
import pandas as pd
import numpy as np
from datetime import datetime
from mesures.headers import AGRECL_HEADER as columns
from mesures.parsers.dummy_data import DummyKeys


class AGRECL(object):
    def __init__(self, data, distributor=None):
        data = DummyKeys(data).data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'AGRECL'
        self.version = 0
        self.default_compression = 'bz2'
        self.distributor = distributor

    def __repr__(self):
        return "{}: {}".format(self.prefix, self.filename)

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        return "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    @property
    def number_of_ups(self):
        return len(list(self.file[self.file['origen'] == 'A']))

    @property
    def number_of_downs(self):
        return len(list(self.file[self.file['origen'] == 'B']))

    def reader(self, file_path):
        if isinstance(file_path, str):
            return pd.read_csv(
                file_path, sep=';', names=columns
            )
        if isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
            if 'tipus_operacio' not in df:
                df['tipus_operacio'] = ''
            if 'tipus_demanda' not in df:
                df['tipus_demanda'] = '0'
            df['data_alta'] = df['data_alta'].apply(lambda x: x.strftime('%Y/%m/%d %H'))
            df['data_baixa'] = df['data_baixa'].apply(
                lambda x: '' if not isinstance(x, pd.Timestamp) else x.strftime('%Y/%m/%d %H'))
            df = df[columns]
            return df

    def writer(self):
        """
        :return: file path of generated AGRECL File
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
