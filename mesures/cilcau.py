# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.cupscau import CUPSCAU
from mesures.headers import CILCAU_HEADER as COLUMNS
from mesures.utils import check_line_terminator_param
import os
import pandas as pd
import numpy as np


class CILCAU(CUPSCAU):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(CILCAU, self).__init__(data, distributor, compression, columns=columns, version=version)
        self.prefix = 'CILCAU'

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
