# -*- coding: utf-8 -*-
from mesures.headers import REOBAGRECL_HEADER as COLUMNS
from mesures.reobjeagrecl import REOBJEAGRECL

import pandas as pd


class REOBAGRECL(REOBJEAGRECL):
    def __init__(self, data, distributor=None, comer=None, periode=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(REOBAGRECL, self).__init__(data, distributor=distributor, comer=comer, periode=periode,
                                      compression=compression, columns=columns, version=version)
        self.prefix = 'REOBAGRECL'
