import pandas as pd
from datetime import datetime
from mesures.headers import P1_HEADER
import os


class P1(object):
    def __init__(self, distributor, filepath):
        self.header = P1_HEADER
        self.file = self.reader(filepath)
        self._total = None
        self._ai = None
        self._ae = None
        self._r1 = None
        self._r2 = None
        self._r3 = None
        self._r4 = None
        self._cups = None
        self._ncups = None
        self.total = 0
        self.ai = 0
        self.ae = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0
        self.r4 = 0
        self.cups = list()
        self.ncups = 0
        self.distributor = distributor
        self.generation_date = datetime.now()
        self.prefix = 'P1'
        self.version = 1

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
        return "{prefix}_{distributor}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, version=self.version
        )

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = self.file['ai'].sum()

    @property
    def ai(self):
        return self._ai

    @ai.setter
    def ai(self, value):
        self._ai = self.file['ai'].sum()

    @property
    def ae(self):
        return self._ae

    @ae.setter
    def ae(self, value):
        self._ae = self.file['ae'].sum()

    @property
    def r1(self):
        return self._r1

    @r1.setter
    def r1(self, value):
        self._r1 = self.file['r1'].sum()

    @property
    def r2(self):
        return self._r2

    @r2.setter
    def r2(self, value):
        self._r2 = self.file['r2'].sum()

    @property
    def r3(self):
        return self._r3

    @r3.setter
    def r3(self, value):
        self._r3 = self.file['r3'].sum()

    @property
    def r4(self):
        return self._r4

    @r4.setter
    def r4(self, value):
        self._r4 = self.file['r4'].sum()

    @property
    def cups(self):
        return self._cups

    @cups.setter
    def cups(self, value):
        self._cups = list(set(self.file['cups']))

    @property
    def ncups(self):
        return self._ncups

    @ncups.setter
    def ncups(self, value):
        self._ncups = len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            return pd.read_csv(
                filepath, sep=';', names=self.header
            )

    def writer(self):
        filepath = os.path.join('tmp', self.filename)
        self.file.to_csv(
            filepath, sep=';', header=False, columns=False, index=False, line_terminator=';'
        )
        return filepath


class P1D(P1):
    def __init__(self, distributor, filepath):
        super(P1D, self).__init__(distributor, filepath)
        self.prefix = 'P1D'

    def writer(self):
        pass
