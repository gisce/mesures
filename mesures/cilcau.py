import pandas as pd
import numpy as np
from mesures.headers import CILCAU_HEADER as columns
from mesures.dates.date import REE_END_DATE
from mesures.cupscau import CUPSCAU

class CILCAU(CUPSCAU):
    def __init__(self, data, distributor='9999'):
        self.prefix = 'CILCAU'
        super(CILCAU, self).__init__(data, distributor=distributor)

    @property
    def cils(self):
        return list(set(self.file['cil']))

    @property
    def number_of_cils(self):
        return len(list(set(self.file['cil'])))

    def reader(self, file_path):
        df = pd.DataFrame(data=file_path)
        df['data_baixa'].fillna(REE_END_DATE, inplace=True)
        df['data_alta'] = df['data_alta'].apply(lambda x: x.strftime('%Y%m%d'))
        df['comentari'] = np.where(df['comentari'], df['comentari'], '')
        return df[columns]
