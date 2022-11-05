# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CUPSDAT_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyKeys
import os
import pandas as pd


class CUPSDAT(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        data = DummyKeys(data).data
        self.columns = columns
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CUPSDAT'
        self.version = 0
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
        filename = "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)
        return filename

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, file_path):
        if isinstance(file_path, str):
            df = pd.read_csv(file_path, sep=';', names=self.columns)
        elif isinstance(file_path, list):
            df = pd.DataFrame(data=file_path)
        else:
            raise Exception("Filepath must be an str or a list")

        df['fecha_hora_inicio_vigencia'] = df.apply(
            lambda row: datetime.strptime(row['fecha_hora_inicio_vigencia'], '%Y-%m-%d %H').strftime(DATE_MASK), axis=1
        )

        df['fecha_hora_final_vigencia'] = df.apply(
            lambda row: REE_END_DATE_HOUR
            if row['fecha_hora_final_vigencia'] == ''
            else datetime.strptime(row['fecha_hora_final_vigencia'], '%Y-%m-%d %H').strftime(DATE_MASK), axis=1)

        return df[self.columns]

    def writer(self):
        """
        :return: file path of generated CUPSDAT File
        """
        file_path = os.path.join('/tmp', self.filename)

        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  'line_terminator': ';\n'
                  }

        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)

        return file_path
