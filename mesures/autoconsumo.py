import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from mesures.headers import AUTOCONSUMO_HEADER
from mesures.curves.curve import DummyCurve
import os
from zipfile import ZipFile


class AUTOCONSUMO(object):
    def __init__(self, data, distributor='9999'):
        self.header = AUTOCONSUMO_HEADER
        self.file = self.reader(data)
        self.distributor = str(distributor)
        self.generation_date = datetime.now()
        self.prefix = 'AUTOCONSUMO'
        self.version = 0

    def __repr__(self):
        return "AUTOCONSUMO: {}".format(self.filename)

    def __eq__(self, other):
        return self.file.equals(other.file)

    def __add__(self, other):
        return self.file.append(other.file)

    def __len__(self):
        return len(self.file)

    @property
    def filename(self):
        return "{prefix}_{distributor}_{timestamp}.{version}".format(
            prefix=self.prefix, distributor=self.distributor,
            timestamp=self.generation_date.strftime('%Y%m%d'), version=self.version
        )

    @property
    def caus(self):
        return list(set(self.file['cau']))

    @property
    def number_of_cups(self):
        return len(list(set(self.file['cups'])))

    def reader(self, filepath):
        if isinstance(filepath, str):
            return pd.read_csv(
                filepath, sep=';', names=self.header
            )
        if isinstance(filepath, list):
            df = pd.DataFrame(data=filepath)
            for key in ('reg_auto_prov', 'reg_auto_def', 'miteco'):
                df[key] = ''
            df['data_baixa'].fillna('30000101')
            df['emmagatzematge'] = np.where(df['emmagatzematge'], 'S', 'N')
            df['codi_postal'] = ''
            df['potencia_nominal'] = ''
            try:
                df = df[AUTOCONSUMO_HEADER]
            except:
                pass
            return df

    def writer(self):
        """
        F1 contains a curve files diary on zip
        :return: file path
        """
        import bz2
        #dataf = self.file[(self.file['timestamp'] >= di) & (self.file['timestamp'] < df)]
        filepath = os.path.join('/tmp', self.filename)
        self.file.to_csv(
            filepath, sep=';', header=False, columns=AUTOCONSUMO_HEADER, index=False, line_terminator=';\n'
        )
        with open(filepath, 'rb') as data:
            f_ = bz2.compress(data.read())
        return filepath
