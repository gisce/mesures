# -*- coding: utf-8 -*-
from mesures.headers import REOBJECIL_HEADER as COLUMNS
from mesures.reobjeagrecl import REOBJEAGRECL

import pandas as pd


class REOBJECIL(REOBJEAGRECL):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBJECIL, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                        compression=compression, columns=COLUMNS, version=version)
        self.prefix = 'REOBJECIL'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=COLUMNS)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['comentari_emissor'] = df.apply(lambda row: row['comentari_emissor'] or '', axis=1)
        df['comentari_receptor'] = df.apply(lambda row: row['comentari_receptor'] or '', axis=1)
        df['motiu_receptor'] = df.apply(lambda row: row['motiu_receptor'] or '', axis=1)
        df['as_publicada'] = df.apply(lambda row: row['as_publicada'] or '', axis=1)
        df['as_proposada'] = df.apply(lambda row: row['as_proposada'] or '', axis=1)
        df['r2_publicada'] = df.apply(lambda row: row['r2_publicada'] or '', axis=1)
        df['r2_proposada'] = df.apply(lambda row: row['r2_proposada'] or '', axis=1)
        df['r3_publicada'] = df.apply(lambda row: row['r3_publicada'] or '', axis=1)
        df['r3_proposada'] = df.apply(lambda row: row['r3_proposada'] or '', axis=1)

        return df
