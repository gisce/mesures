# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CILDAT_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyKeys
from mesures.utils import check_line_terminator_param
import os
import pandas as pd
import numpy as np


class CILDAT(object):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CILDAT'
        self.version = version
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
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
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
            df = pd.read_csv(file_path, sep=';', names=self.columns)
        elif isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
        else:
            raise Exception("Filepath must be an str or a list")

        df['fecha_alta'] = pd.to_datetime(df['fecha_alta'])
        df['fecha_alta'] = df['fecha_alta'].dt.strftime(SIMPLE_DATE_MASK)

        df['fecha_baja'] = pd.to_datetime(df['fecha_baja'], errors='coerce')
        df['fecha_baja'] = np.where(
            df['fecha_baja'].apply(lambda x: isinstance(x, pd.Timestamp)),
            df['fecha_baja'].dt.strftime(SIMPLE_DATE_MASK),
            REE_END_DATE
        )

        df['fecha_acta_servicio'] = pd.to_datetime(df['fecha_acta_servicio'], errors='coerce')
        df['fecha_acta_servicio'] = df['fecha_acta_servicio'].dt.strftime(SIMPLE_DATE_MASK)

        return df[self.columns]

    def writer(self):
        """
        :return: file path of generated CILDAT File
        """
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
