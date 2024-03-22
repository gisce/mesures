# -*- coding: utf-8 -*-
from mesures.a5d import A5D


class B5D(A5D):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(B5D, self).__init__(data, distributor=distributor, comer=comer, compression=compression, version=version)
        self.prefix = 'B5D'
