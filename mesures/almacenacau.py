import os
import pandas as pd
import numpy as np
from datetime import datetime
from mesures.headers import ALMACENACAU_HEADER as columns
from mesures.dates.date import REE_END_DATE
from mesures.parsers.dummy_data import DummyKeys

class ALMACENACAU(object):
    def __init__(self, data, distributor=None):
        data = DummyKeys(data).data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'ALMACENACAU'
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

    def reader(self, file_path):
        if isinstance(file_path, str):
            return pd.read_csv(
                file_path, sep=';', names=columns
            )
        if isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
            df['data_baixa'] = df['data_baixa'].apply(
                lambda x: REE_END_DATE if not isinstance(x, pd.Timestamp) else x.strftime('%Y%m%d'))
            df['data_alta'] = df['data_alta'].apply(lambda x: x.strftime('%Y%m%d'))
            df['tecnologia_emmagatzematge'] = df['tecnologia_emmagatzematge'].astype(str)
            df['tecnologia_emmagatzematge'] = df['tecnologia_emmagatzematge'].apply(lambda x: x.zfill(2))
            try:
                df['comentari'] = np.where(df['comentari'], df['comentari'], '')
            except KeyError:
                df['comentari'] = ''
            return df[columns]

    def writer(self):
        """
        :return: file path of generated ALMACENACAU File
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
