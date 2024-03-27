# -*- coding: utf-8 -*-
from mesures.a5d import A5D
from mesures.dates import *
from mesures.headers import A5D_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
import pandas as pd


class B5D(A5D):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'B5D'
        self.default_compression = compression
        self.version = version
        self.distributor = distributor
        self.comer = comer

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=self.columns
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df = df.groupby(['cups', 'timestamp', 'season', 'factura']).aggregate(
            {'ai': 'sum', 'ae': 'sum',
             'r1': 'sum', 'r2': 'sum', 'r3': 'sum', 'r4': 'sum'}
        ).reset_index()
        df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
        for key in ['method', 'firmeza']:
            df[key] = ''
        df = df[self.columns]
        return df
