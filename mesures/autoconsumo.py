# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import AUTOCONSUMO_HEADER as columns
from mesures.parsers.dummy_data import DummyKeys
from mesures.utils import check_line_terminator_param
import os
import pandas as pd
import numpy as np


class AUTOCONSUMO(object):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.columns = columns
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'AUTOCONSUMO'
        self.version = version
        self.default_compression = compression
        self.distributor = distributor

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
        if self.default_compression:
            return "{prefix}_{distributor}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )

    @property
    def caus(self):
        return list(set(self.file['cau']))

    @property
    def number_of_caus(self):
        return len(list(set(self.file['cau'])))

    def reader(self, file_path):
        if isinstance(file_path, str):
            df = pd.read_csv(file_path, sep=';', names=self.columns)
        elif isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
        else:
            raise Exception("Filepath must be an str or a list")

        df['data_alta'] = pd.to_datetime(df['data_alta'])
        df['data_alta'] = df['data_alta'].dt.strftime(SIMPLE_DATE_MASK)

        df['data_baixa'] = pd.to_datetime(df['data_baixa'], errors='coerce')
        df['data_baixa'] = np.where(
            df['data_baixa'].apply(lambda x: isinstance(x, pd.Timestamp)),
            df['data_baixa'].dt.strftime(SIMPLE_DATE_MASK),
            REE_END_DATE
        )

        df['emmagatzematge'] = np.where(df['emmagatzematge'], 'S', 'N')

        df['subgrup'] = df['subgrup'].apply(lambda x: '{}.{}.{}'.format(x[0], x[1], x[2]) if x != '' else '')

        df['tipus_antiabocament'] = (
            df['tipus_antiabocament'].apply(lambda x: '' if (x == 0 or not x or x == '') else x))

        try:
            df = df[self.columns]
        except:
            # Fins que entri en vigor el nou fitxer, traiem 'estat' de la llista d'índexs del df.
            self.columns.remove('estat')
            df = df[self.columns]

        return df

    def writer(self):
        """
        :return: file path of generated AUTOCONSUMO File
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
