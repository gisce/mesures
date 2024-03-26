# -*- coding: utf-8 -*-
from mesures.headers import P2_HEADER as COLUMNS
from mesures.p1 import P1


class P2(P1):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P2, self).__init__(data, distributor, compression=compression, columns=columns, version=version)
        self.prefix = 'P2'
