from mesures.p1 import P1
from mesures.headers import P1_HEADER as columns

class P2(P1):
    def __init__(self, data, distributor=None):
        super(P2, self).__init__(data, distributor)
        self.prefix = 'P2'

    def reader(self):
        for key in ['ai', 'ae', 'r1', 'r2', 'r3', 'r4']:
            if key not in df:
                df[key] = 0
            df[key] = df[key].astype('int32')

    def writer(self):
        """
        P2 contains a curve files diary on zip
        :return: file path
        """
        return super(P2, self).writer()
