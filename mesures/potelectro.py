# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import POTELECTRO_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
from zipfile import ZipFile
import os
import pandas as pd


class POTELECTRO(object):
    def __init__(self, data, distributor=None, compression='bz2'):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'POTELECTRO'
        self.version = 0
        self.distributor = distributor
        self.default_compression = compression

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        if self.default_compression:
            return "{prefix}_{distributor}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor,
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor,
            timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")
        # TODO clean "powers" for new supply points
        # TODO clean "projections" for new supply points
        # TODO use "projection" only under REE request ("G" field on CUPSELECTRO)
        df = df[columns]
        return df

    def writer(self):
        """
        POTELECTRO contains a curve files diary on zip
        :return: file path
        """
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        filepath = os.path.join('/tmp', self.filename)
        self.file.to_csv(
            filepath, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        zipped_file.write(filepath, arcname=os.path.basename(filepath))
        zipped_file.close()
        return zipped_file.filename