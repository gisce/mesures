# -*- coding: utf-8 -*-
from mesures.dates import *
from mesures.p1 import P1
from mesures.utils import check_line_terminator_param
from mesures.headers import P1REG_HEADER as COLUMNS
from zipfile import ZipFile
import pandas as pd
import os
from datetime import datetime


class P1REG(P1):
    def __init__(self, data, concentrador, measure_date, compression='bz2', columns=COLUMNS, version=0):
        super(P1REG, self).__init__(data, distributor=concentrador, compression=compression, columns=columns, version=version)

        self.prefix = 'P1REG'
        self.concentrador = concentrador

        if hasattr(measure_date, 'strftime'):
            self.measure_date_str = measure_date.strftime('%Y%m%d')
        else:
            self.measure_date_str = str(measure_date).replace('-', '').replace('/', '')[:8]

    def reader(self, filepath):
        if isinstance(filepath, str):
            df = pd.read_csv(filepath, sep=';', names=self.columns)
        elif isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
        else:
            raise Exception("Filepath must be an str or a list")

        df = df[self.columns]
        return df

    @property
    def cups(self):
        return list(set(self.file['codigo_pm']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['codigo_pm'])))

    @property
    def filename(self):
        filename = "{prefix}_{concentrador}_{measure_date}_{timestamp}.{version}".format(
            prefix=self.prefix,
            concentrador=self.concentrador,
            measure_date=self.measure_date_str,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
            version=self.version
        )

        if self.default_compression:
            filename += ".{compression}".format(compression=self.default_compression)
        return filename

    @property
    def zip_filename(self):
        return "{prefix}_{concentrador}_{measure_date}_{timestamp}.{version}.zip".format(
            prefix=self.prefix,
            concentrador=self.concentrador,
            measure_date=self.measure_date_str,
            timestamp=self.generation_date.strftime(SIMPLE_DATE_MASK),
            version=self.version
        )

    def writer(self):
        existing_files = os.listdir('/tmp')

        if existing_files:
            zip_versions = [int(f.split('.')[1])
                            for f in existing_files if self.zip_filename.split('.')[0] in f and '.zip' in f]
            if zip_versions:
                self.version = max(zip_versions) + 1

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

        zip_path = os.path.join('/tmp', self.zip_filename)
        zipped_file = ZipFile(zip_path, 'w')
        zipped_file.write(file_path, arcname=os.path.basename(file_path))
        zipped_file.close()

        os.remove(file_path)

        return zip_path

    @staticmethod
    def get_ita_timestamp(dt, is_summer_time):
        if isinstance(dt, str):
            dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

        is_summer = bool(int(is_summer_time))

        minute = dt.minute
        hour = dt.hour
        if is_summer:
            hour |= 0x80

        day = dt.day
        dow = dt.isoweekday()
        day_byte = day | (dow << 5)

        month = dt.month
        year = dt.year % 100

        return "{:02X}{:02X}{:02X}{:02X}{:02X}".format(minute, hour, day_byte, month, year)