# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CUPS45_HEADER as COLUMNS
from mesures.cupsdat import CUPSDAT
from mesures.parsers.dummy_data import DummyKeys


class CUPS45(CUPSDAT):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CUPS45'
        self.version = 0
        self.default_compression = compression
        self.distributor = distributor
