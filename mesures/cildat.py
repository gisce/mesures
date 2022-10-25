# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CILDAT_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyKeys
import os
import pandas as pd


class CILDAT(object):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CILDAT'
        self.version = 0
        self.default_compression = compression
        self.distributor = distributor
        self.columns = COLUMNS

    def __repr__(self):
        return "{}: {}".format(self.prefix, self.filename)

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        filename = "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix,
            distributor=self.distributor,
            timestamp=self.generation_date.strftime('%Y%m%d'),
            version=self.version)
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

    def reader(self, file_path):
        if isinstance(file_path, str):
            df = pd.read_csv(file_path, sep=';', names=COLUMNS)
        elif isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
        else:
            raise Exception("Filepath must be an str or a list")

        df['fecha_alta'] = df.apply(lambda row: row['fecha_alta'].strftime('%Y%m%d'), axis=1)
        df['fecha_baja'] = df.apply(lambda row: REE_END_DATE
                                    if not isinstance(row['fecha_baja'], pd.Timestamp)
                                    else row['fecha_baja'].strftime('%Y%m%d'),
                                    axis=1)
        df['fecha_acta_servicio'] = df.apply(lambda row: row['fecha_acta_servicio'].strftime('%Y%m%d'), axis=1)

        return df[COLUMNS]

    def writer(self):
        """
        :return: file path of generated CILDAT File
        """
        file_path = os.path.join('/tmp', self.filename)

        kwargs = {'sep': ';',
                  'header': False,
                  'columns': COLUMNS,
                  'index': False,
                  'line_terminator': ';\n'
                  }

        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)

        return file_path
