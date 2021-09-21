# -*- coding: utf-8 -*-
from datetime import datetime
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.f5 import F5
import os
import pandas as pd


class F5D(F5):
    def __init__(self, data, distributor=None, comer=None):
        super(F5D, self).__init__(data, distributor, comer)
        self.prefix = 'F5D'
        self.default_compression = 'bz2'

    @property
    def filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    def writer(self):
        """
        F5D contains a hourly invoiced curve
        :return: file path
        """
        self.file['timestamp'] = self.file['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=COLUMNS, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
