# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import ALMACENACAU_HEADER as columns
from mesures.parsers.dummy_data import DummyKeys
from mesures.utils import check_line_terminator_param
import os
import numpy as np
import pandas as pd


class ALMACENACAU(object):
    def __init__(self, data, distributor=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'ALMACENACAU'
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
                timestamp=self.generation_date.strftime('%Y%m%d'),
                version=self.version, compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    def reader(self, file_path):
        if isinstance(file_path, str):
            df = pd.read_csv(
                file_path, sep=';', names=columns
            )
        elif isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
        else:
            raise Exception("Filepath must be an str or a list")

        df['data_baixa'] = df['data_baixa'].apply(
            lambda x: REE_END_DATE if not isinstance(x, pd.Timestamp) else x.strftime('%Y%m%d'))
        df['data_alta'] = df['data_alta'].apply(lambda x: x.strftime('%Y%m%d'))
        df['tecnologia_emmagatzematge'] = df['tecnologia_emmagatzematge'].astype(str)
        try:
            df['comentari'] = np.where(df['comentari'], df['comentari'], '')
        except KeyError:
            df['comentari'] = ''
        return df[columns]

    def writer(self):
        """
        :return: file path of generated ALMACENACAU File
        """
        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': columns,
                  'index': False,
                  check_line_terminator_param(): ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
