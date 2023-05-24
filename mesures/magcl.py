# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import MAGCL_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
import os
import pandas as pd


class MAGCL(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = columns
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'MAGCL'
        self.version = version
        self.distributor = distributor
        self.default_compression = compression

    def __repr__(self):
        return "{}: {} kWh".format(self.filename, self.total)

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
        filename = "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                measures_date=self.measures_date[:10].replace('/', ''),
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )
        if self.default_compression:
            filename += ".{compression}".format(compression=self.default_compression)

        return filename

    @property
    def total(self):
        return float(self.file[self.file['magnitud' == 'AE']]['consum'].sum())

    @property
    def ai(self):
        return float(self.file[self.file['magnitud' == 'AE']]['consum'].sum())

    @property
    def ae(self):
        return float(self.file[self.file['magnitud' == 'AS']]['consum'].sum())

    @property
    def r1(self):
        return float(self.file[self.file['magnitud' == 'R1']]['consum'].sum())

    @property
    def r2(self):
        return float(self.file[self.file['magnitud' == 'R2']]['consum'].sum())

    @property
    def r3(self):
        return float(self.file[self.file['magnitud' == 'R3']]['consum'].sum())

    @property
    def r4(self):
        return float(self.file[self.file['magnitud' == 'R4']]['consum'].sum())

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        # TODO data processing

        df = df[self.columns]
        return df

    def writer(self):
        existing_files = os.listdir('/tmp')
        if existing_files:
            versions = [int(f.split('.')[1]) for f in existing_files if self.filename.split('.')[0] in f]
            if versions:
                self.version = max(versions) + 1

        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  check_line_terminator_param(): ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
