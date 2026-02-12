# -*- coding: utf-8 -*-
from mesures.headers import REOBCIL_HEADER as COLUMNS
from mesures.reobjecil import REOBJECIL

import pandas as pd


class REOBCIL(REOBJECIL):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBCIL, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                        compression=compression, columns=columns, version=version)
        self.prefix = 'REOBCIL'
