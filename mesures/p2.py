import pandas as pd
from mesures.p1 import P1


class P2(P1):
    def __init__(self, distributor, filepath):
        super(P2, self).__init__(distributor, filepath)
        self.prefix = 'P2'
        self.header = 'P2_HEADER'

    def writer(self):
        pass


class P2D(P2):
    def __init__(self, distributor, filepath):
        super(P2D, self).__init__(distributor, filepath)
        self.prefix = 'P1D'
        self.header = 'P2_HEADER'

    def writer(self):
        pass
