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
                                         compression=compression, columns=columns, version=version)
        self.prefix = 'REOBJEINCL'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        for col in ['comentari_emissor', 'comentari_receptor', 'motiu_receptor',
                    'energia_entrant_publicada', 'energia_entrant_proposada',
                    'energia_sortint_publicada', 'energia_sortint_proposada']:
            if col not in df.columns:
                df[col] = ''
            else:
                df[col] = df[col].fillna('')

        return df
