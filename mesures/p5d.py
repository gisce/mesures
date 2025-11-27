# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import P5D_HEADER as COLUMNS
from mesures.parsers.dummy_data import DummyCurve
from mesures.utils import check_line_terminator_param
from zipfile import ZipFile
import os
import pandas as pd


class P5D(object):
    def __init__(self, data, distributor=None, comer=None, compression='bz2', version=0):
        """
        :param data: list of dicts or absolute file_path
        :param distributor: str distributor REE code
        :param comer: str comer REE code
        :param compression: 'bz2', 'gz'... OR False otherwise
        """
        if isinstance(data, list):
            data = DummyCurve(data).curve_data
        self.columns = COLUMNS
        self.file = self.reader(data)
        self.generation_date = datetime.now()
        self.prefix = 'P5D'
        self.default_compression = compression
        self.version = version
        self.distributor = distributor
        self.comer = comer

    def __repr__(self):
        return "{}: {} Wh".format(self.filename, self.total)

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        filename = "{prefix}_{distributor}_{comer}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor, comer=self.comer,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK), version=self.version
            )
        if self.default_compression:
            filename += '.{compression}'.format(compression=self.default_compression)
        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{comer}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor,
            comer=self.comer,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK)
        )

    @property
    def total(self):
        return int(self.file['ai'].sum())

    @property
    def ai(self):
        return int(self.file['ai'].sum())

    @property
    def ae(self):
        return int(self.file['ae'].sum())

    @property
    def cups(self):
        return list(set(self.file['cups']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df = df.groupby(
            ['cups', 'timestamp', 'season']
        ).aggregate(
            {'ai': 'sum',
             'ae': 'sum'}
        ).reset_index()

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].dt.strftime(DATETIME_HOUR_MASK)

        for key in ['ai', 'ae']:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')

        df = df[self.columns]
        return df

    def writer(self):
        """
        P5D contains an hourly raw curve
        :return: file path
        """
        existing_files = os.listdir('/tmp')
        if existing_files and self.default_compression != 'zip':
            versions = [int(f.split('.')[1])
                        for f in existing_files if self.filename.split('.')[0] in f and '.zip' not in f]
            if versions:
                self.version = max(versions) + 1

        file_path = os.path.join('/tmp', self.filename)
        kwargs = {'sep': ';',
                  'header': False,
                  'columns': self.columns,
                  'index': False,
                  check_line_terminator_param(): ';\n'
                  }
        if self.default_compression:
            kwargs.update({'compression': self.default_compression})

        if kwargs.get('compression', False) == 'zip':
            self.default_compression = False
            zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
            file_path = os.path.join('/tmp', self.filename)
            kwargs.pop('compression')
            self.file.to_csv(file_path, **kwargs)
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
            file_path = zipped_file.filename
        else:
            self.file.to_csv(file_path, **kwargs)
        return file_path
