# -*- coding: utf-8 -*-
from datetime import datetime
from mesures.headers import F5D_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
import os
import pandas as pd


class F5(object):
    def __init__(self, data, distributor=None, comer=None):
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'F5'
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
        return "{prefix}_{distributor}_{comer}_{measures_date}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer, measures_date=self.measures_date.strftime('%Y%m%d')
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
            if 'firmeza' not in df:
                    df['firmeza'] = df['method'].apply(lambda x: 1 if x in (1, 3) else 0)
            df = df[COLUMNS]
            return df

    def writer(self):
        """
        F5 contains a curve files diary on zip
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        #todo: get a zip filename without measures_date
        zipped_file = ZipFile(os.path.join('/tmp', self.filename + '.zip'), 'w')
        while daymin <= daymax:
            di = daymin
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            dataf['timestamp'] = dataf['timestamp'].apply(lambda x: x.strftime('%Y/%m/%d %H:%M:%S'))
            filepath = os.path.join('/tmp', self.filename) + '.' + self.default_compression
            dataf.to_csv(
                filepath, sep=';', header=False, columns=COLUMNS, index=False, line_terminator=';\n'
            )
            daymin = df
            zipped_file.write(filepath, arcname=os.path.basename(filepath))
        zipped_file.close()
        return zipped_file.filename
