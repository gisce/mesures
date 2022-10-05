# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.headers import F3_HEADER as columns
from mesures.parsers.dummy_data import DummyCurve
from zipfile import ZipFile
import os
import pandas as pd


class F3(object):
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
        self.prefix = 'F3'
        self.version = 0
        self.distributor = distributor
        self.default_compression = compression

    def __repr__(self):
        return "{}: {} kWh".format(self.filename, self.total)

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
        if self.default_compression:
            return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}.{compression}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version,
                compression=self.default_compression
            )
        else:
            return "{prefix}_{distributor}_{measures_date}_{timestamp}.{version}".format(
                prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
                timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
            )

    @property
    def zip_filename(self):
        return "{prefix}_{distributor}_{measures_date}_{timestamp}.zip".format(
            prefix=self.prefix, distributor=self.distributor, measures_date=self.measures_date.strftime('%Y%m'),
            timestamp=self.generation_date.strftime('%Y%m%d')
        )

    @property
    def total(self):
        return self.file['ai'].sum()

    @property
    def ai(self):
        return self.file['ai'].sum()

    @property
    def ae(self):
        return self.file['ae'].sum()

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

        df = df.groupby(
            ['cups', 'timestamp', 'season']
        ).aggregate(
            {
                'ai': 'sum',
                'ae': 'sum'
            }
        ).reset_index()
        # TODO review obtencion and firmeza
        df['method'] = 1
        df['firmeza'] = 1
        df = df[columns]
        return df

    def writer(self):
        """
        F1 contains a curve files diary on zip
        :return: file path
        """
        daymin = self.file['timestamp'].min()
        daymax = self.file['timestamp'].max()
        self.measures_date = daymin
        zipped_file = ZipFile(os.path.join('/tmp', self.zip_filename), 'w')
        while daymin <= daymax:
            di = daymin
            df = daymin + timedelta(days=1)
            self.measures_date = di
            dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
            dataf['timestamp'] = dataf.apply(lambda row: row['timestamp'].strftime(REE_ELECTROINTENSIVO_DATETIME_MASK),
                                             axis=1)
            file_path = os.path.join('/tmp', self.filename)
            kwargs = {'sep': ';',
                      'header': False,
                      'columns': columns,
                      'index': False,
                      'line_terminator': ';\n'
                      }
            if self.default_compression:
                kwargs.update({'compression': self.default_compression})

            dataf.to_csv(file_path, **kwargs)
            daymin = df
            zipped_file.write(file_path, arcname=os.path.basename(file_path))
        zipped_file.close()
        return zipped_file.filename
