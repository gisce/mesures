# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CUPSCAU_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyKeys
from mesures.utils import check_line_terminator_param
import os
import pandas as pd
import numpy as np


class CUPSCAU(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.columns = columns
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CUPSCAU'
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
                prefix=self.prefix, distributor=self.distributor, timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
                version=self.version, compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

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

        try:
            df['comentari'] = np.where(df['comentari'], df['comentari'], '')
        except KeyError:
            df['comentari'] = ''

        return df[self.columns]

    def writer(self):
        """
        :return: file path of generated CUPSCAU File
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
