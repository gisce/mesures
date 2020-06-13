from mesures.p1 import P1

class P2(P1):
    def __init__(self, data, distributor=None):
        super(P2, self).__init__(data, distributor)
        self.prefix = 'P2'

    def writer(self):
        pass
