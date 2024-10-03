# -*- coding: utf-8 -*-
from mesures.headers import OBCUPS_HEADER as COLUMNS
from mesures.obagrecl import OBAGRECL


class OBCUPS(OBAGRECL):
    def __init__(self, data, emissor=None, distribuidora=None, periode=None, compression='bz2', columns=COLUMNS,
                 version=0):
        """
        :param data: list of dicts or absolute file_path
        :param emissor: str emissor REE code
        :param distribuidora: str distribuidora REE code
        :param periode: str e.g. '202401'
        :param compression: 'bz2', 'gz'... OR False otherwise
        :param columns: list
        :param version: int
        """
        super(OBCUPS, self).__init__(data, emissor=emissor, distribuidora=distribuidora, periode=periode,
                                      compression=compression, columns=COLUMNS, version=version)
        self.prefix = 'OBCUPS'
