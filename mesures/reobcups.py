# -*- coding: utf-8 -*-
from mesures.headers import REOBCUPS_HEADER as COLUMNS
from mesures.reobje2 import REOBJE2

import pandas as pd


class REOBCUPS(REOBJE2):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBCUPS, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                      compression=compression, columns=columns, version=version)
        self.prefix = 'REOBCUPS'
