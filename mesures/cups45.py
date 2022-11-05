# -*- coding: utf-8 -*-
from mesures.headers import CUPS45_HEADER as COLUMNS
from mesures.cupsdat import CUPSDAT


class CUPS45(CUPSDAT):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(CUPS45, self).__init__(data, distributor=distributor, compression=compression, columns=columns)
        self.prefix = 'CUPS45'
