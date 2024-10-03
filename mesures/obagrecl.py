# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import OBAGRECL_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
import os
import pandas as pd


class OBAGRECL(object):
    def __init__(self, data, emissor=None, distribuidora=None, periode=None, compression='bz2', columns=COLUMNS,
                 version=0):
        """
        :param data: list of dicts or absolute file_path
        :param emissor: str emissor REE code
        :param distribuidora: str distribuïdora REE code
        :param periode: str e.g. '202401'
        :param compression: 'bz2', 'gz'... OR False otherwise
        :param columns: list
        :param version: int
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'OBAGRECL'
        self.version = version
        self.emissor = emissor
        self.distribuidora = distribuidora
        self.default_compression = compression
        self.periode = periode
        self.columns = columns

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        filename = "{prefix}_{emissor}_{distribuidora}_{periode}_{timestamp}.{version}".format(
            prefix=self.prefix,
            emissor=self.emissor,
            distribuidora=self.distribuidora,
            periode=self.periode,
            timestamp=self.generation_date.strftime('%Y%m%d'),
            version=self.version
            )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)

        return filename

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=COLUMNS)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df['comentari_emissor'] = df.apply(lambda row: row['comentari_emissor'] or '', axis=1)
        df['energia_publicada'] = df.apply(lambda row: row['energia_publicada'] or '', axis=1)
        df['energia_proposada'] = df.apply(lambda row: row['energia_proposada'] or '', axis=1)

        return df

    def writer(self):
        """
        OBAGRECL TMP file generattion
        :return: file path
        """
        # Check and change value version of file
        existing_files = os.listdir('/tmp')
        if existing_files:
            versions = [int(f.split('.')[1]) for f in existing_files if self.filename.split('.')[0] in f]
            if versions:
                self.version = max(versions) + 1

        # Generate file path
        file_path = os.path.join('/tmp', self.filename)

        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  'float_format': '%.2f',
                  check_line_terminator_param(): ';\n',
                  'encoding': 'iso-8859-15',
                  }

        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        # Convert dict data to csv file and save it to the file path generated
        self.file.to_csv(file_path, **kwargs)

        # Return location tmp file
        return file_path
