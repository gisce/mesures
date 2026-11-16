# -*- coding: utf-8 -*-
from mesures.p1reg import P1REG
from mesures.headers import P1REG_HEADER as COLUMNS

class P1REGQH(P1REG):
    def __init__(self, data, concentrador, measure_date, compression='bz2', columns=COLUMNS, version=0):
        super(P1REGQH, self).__init__(data, concentrador, measure_date, compression=compression, columns=columns, version=version)

        self.prefix = 'P1REGQH'