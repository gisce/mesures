# -*- coding: utf-8 -*-
from mesures.headers import REOBJE2_HEADER as COLUMNS
from mesures.reobjeagrecl import REOBJEAGRECL

import pandas as pd


class REOBJE2(REOBJEAGRECL):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBJE2, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                      compression=compression, columns=COLUMNS, version=version)
        self.prefix = 'REOBJE2'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=COLUMNS)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['comentari_emissor'] = df.apply(lambda row: row['comentari_emissor'] or '', axis=1)
        df['comentari_receptor'] = df.apply(lambda row: row['comentari_receptor'] or '', axis=1)
        df['energia_publicada'] = df.apply(lambda row: row['energia_publicada'] or '', axis=1)
        df['energia_proposada'] = df.apply(lambda row: row['energia_proposada'] or '', axis=1)

        return df
