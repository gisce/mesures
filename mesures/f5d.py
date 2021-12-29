# -*- coding: utf-8 -*-
from datetime import datetime
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.f5 import F5
import os
import pandas as pd


class F5D(F5):
    def __init__(self, data, distributor=None, comer=None, compression='bz2'):
        super(F5D, self).__init__(data, distributor, comer)
        self.prefix = 'F5D'
        self.default_compression = compression

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

    def cut_by_dates(self, di, df):
        """
        Cut File by dates, discard > and <
        :param di: str datetime LIKE 2021-01-01 01:00
        :param df: str datetime LIKE 2021-02-01 00:00
        """
        self.file = self.file[(self.file.timestamp >= di) & (self.file.timestamp <= df)]

    def reader(self, filepath):
        df = super(F5D, self).reader(filepath)
        try:
            df['timestamp'] = df['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M'))
        except Exception as err:
            # Timestamp is already well parsed
            pass
        finally:
            return df

    def writer(self):
        """
        F5D contains a hourly invoiced curve
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename)
        self.file.to_csv(
            file_path, sep=';', header=False, columns=COLUMNS, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
