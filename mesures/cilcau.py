import os
import pandas as pd
import numpy as np
from mesures.headers import CILCAU_HEADER as columns
from mesures.dates.date import REE_END_DATE
from mesures.cupscau import CUPSCAU

class CILCAU(CUPSCAU):
    def __init__(self, data, distributor=None):
        super(CILCAU, self).__init__(data, distributor)
        self.prefix = 'CILCAU'

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

    def reader(self, file_path):
        df = pd.DataFrame(data=file_path)
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
        file_path = os.path.join('/tmp', self.filename) + '.' + self.default_compression
        self.file.to_csv(
            file_path, sep=';', header=False, columns=columns, index=False, line_terminator=';\n',
            compression=self.default_compression
        )
        return file_path
