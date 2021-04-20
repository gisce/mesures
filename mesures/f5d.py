# -*- coding: utf-8 -*-
from datetime import datetime
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
import os
import pandas as pd


class F5D(object):
    def __init__(self, data, distributor=None, comer=None):
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'F5D'
        self.default_compression = 'bz2'
        self.version = 0
        self.distributor = distributor
        self.comer = comer

    def __repr__(self):
        return "{}: {} Wh".format(self.filename, self.total)

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    @property
    def total(self):
        return self.file['ai'].sum()

    @property
    def ai(self):
        return self.file['ai'].sum()

    @property
    def ae(self):
        return self.file['ae'].sum()

    @property
    def r1(self):
        return self.file['r1'].sum()

    @property
    def r2(self):
        return self.file['r2'].sum()

    @property
    def r3(self):
        return self.file['r3'].sum()

    @property
    def r4(self):
        return self.file['r4'].sum()

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    @property
    def number_of_invoices(self):
        return len(list(set(self.file['factura'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            return pd.read_csv(
                filepath, sep=';', names=COLUMNS
            )
        if isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
            df = df[COLUMNS]
            return df

    def writer(self):
        """
        F5D contains a hourly invoiced curve
        :return: file path
        """
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=COLUMNS, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
