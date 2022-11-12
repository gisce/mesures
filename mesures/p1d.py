# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import P1_HEADER as COLUMNS
from mesures.p1 import P1


class P1D(P1):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', columns=COLUMNS):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P1D, self).__init__(data, distributor=distributor, compression=compression, columns=columns)
        self.prefix = 'P1D'
        self.comer = comer

    @property
    def filename(self):
        filename = "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )
        if self.default_compression:
            filename += ".{compression}".format(compression=self.default_compression)

        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor,
            comer=self.comer,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK)
        )
