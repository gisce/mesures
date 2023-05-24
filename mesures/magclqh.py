# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MAGCL_HEADER as COLUMNS
from mesures.magcl import MAGCL
import pandas as pd


class MAGCLQH(MAGCL):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(MAGCLQH, self).__init__(data=data, distributor=distributor, compression=compression, columns=columns,
                                      version=version)
        self.prefix = 'MAGCLQH'

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        # TODO data processing

        df = df[self.columns]
        return df
