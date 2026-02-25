# -*- coding: utf-8 -*-
from mesures.pmest import PMEST


class PMESTQH(PMEST):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(PMESTQH, self).__init__(data, distributor, compression=compression, version=version)
        self.prefix = 'PMESTQH'
