# -*- coding: utf-8 -*-
from mesures.headers import P1_HEADER as columns
from mesures.p1 import P1
import os


class P1D(P1):
    def __init__(self, data, distributor=None, comer=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(P1D, self).__init__(data, distributor, compression)
        self.prefix = 'P1D'
        self.comer = comer

    @property
    def filename(self):
        if self.default_compression:
            return "{prefix}_{distributor}_{comer}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, comer=self.comer,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    def writer(self):
        """
        P1D contains all curve measure in one file
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename)
        self.file['timestamp'] = self.file.apply(lambda row: row['timestamp'].strftime('%Y/%m/%d %H:%M:%S'), axis=1)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': columns,
                  'index': False,
                  'line_terminator': ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
