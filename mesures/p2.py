# -*- coding: utf-8 -*-
from mesures.headers import P2_HEADER as columns
from mesures.p1 import P1
import pandas as pd


class P2(P1):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P2, self).__init__(data, distributor, compression)
        self.prefix = 'P2'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(
                filepath, sep=';', names=columns
            )
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['tipo_medida'] = 11
        df.groupby(['cups', 'tipo_medida', 'timestamp', 'season']).aggregate({'ai': 'sum'})
        df['method'] = 1
        df['firmeza'] = 1
        df['res'] = 0
        df['res2'] = 0
        for key in columns:
            if 'quality' in key and key not in df:
                df[key] = 0
        for key in ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')
        df = df[columns]
        return df

    def writer(self):
        """
        P2 contains a curve files diary on zip
        :return: file path
        """
        return super(P2, self).writer()
