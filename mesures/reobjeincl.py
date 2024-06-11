# -*- coding: utf-8 -*-
from mesures.headers import REOBJEINCL_HEADER as COLUMNS
from mesures.reobjeagrecl import REOBJEAGRECL
import pandas as pd


class REOBJEINCL(REOBJEAGRECL):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBJEINCL, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                         compression=compression, columns=COLUMNS, version=version)
        self.prefix = 'REOBJEINCL'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=COLUMNS)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['comentari_receptor'] = df.apply(lambda row: row['comentari_receptor'] or '', axis=1)
        df['energia_entrant_publicada'] = df.apply(lambda row: row['energia_entrant_publicada'] or '', axis=1)
        df['energia_entrant_proposada'] = df.apply(lambda row: row['energia_entrant_proposada'] or '', axis=1)
        df['energia_sortint_publicada'] = df.apply(lambda row: row['energia_sortint_publicada'] or '', axis=1)
        df['energia_sortint_proposada'] = df.apply(lambda row: row['energia_sortint_proposada'] or '', axis=1)

        return df
