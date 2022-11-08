# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.cupscau import CUPSCAU
from mesures.headers import CILCAU_HEADER as columns
import os
import numpy as np
import pandas as pd


class CILCAU(CUPSCAU):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        super(CILCAU, self).__init__(data, distributor, compression)
        self.prefix = 'CILCAU'

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

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
        try:
            df['comentari'] = np.where(df['comentari'], df['comentari'], '')
        except KeyError:
            df['comentari'] = ''
        return df[columns]

    def writer(self):
        """
        :return: file path of generated CUPSCAU File
        """
        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': columns,
                  'index': False,
                  'line_terminator': ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)
        return file_path
