# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import CUPSDAT_HEADER as COLUMNS, CUPSDAT_HEADER_2024 as COLUMNS_2024
from mesures.parsers.dummy_data import DummyKeys
from mesures.utils import check_line_terminator_param
import os
import pandas as pd
import numpy as np


class CUPSDAT(object):
    def __init__(self, data, distributor=None, compression='bz2', columns=COLUMNS, include_measure_type_indicator=False,
                 version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        :param include_measure_type_indicator: boolean (indicates if new columns is included)
        """
        data = DummyKeys(data).data
        self.columns = columns
        if include_measure_type_indicator:
            self.columns = COLUMNS_2024
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'CUPSDAT'
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
        filename = "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
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

        df['fecha_hora_inicio_vigencia'] = pd.to_datetime(df['fecha_hora_inicio_vigencia'])
        df['fecha_hora_inicio_vigencia'] = df['fecha_hora_inicio_vigencia'].dt.strftime(DATE_MASK)

        df['fecha_hora_final_vigencia'] = pd.to_datetime(df['fecha_hora_final_vigencia'], errors='coerce')
        df['fecha_hora_final_vigencia'] = np.where(
            df['fecha_hora_final_vigencia'].apply(lambda x: isinstance(x, pd.Timestamp)),
            df['fecha_hora_final_vigencia'].dt.strftime(DATE_MASK),
            CUPSDAT_CPUS45_REE_END_DATE_HOUR
        )

        return df[self.columns]

    def writer(self):
        """
        :return: file path of generated CUPSDAT File
        """
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
                  'encoding': 'iso-8859-15',
                  check_line_terminator_param(): ';\n'
                  }

        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        self.file.to_csv(file_path, **kwargs)

        return file_path
