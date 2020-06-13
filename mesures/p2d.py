from mesures.p2 import P2

class P2D(P2):
    def __init__(self, data, distributor=None):
        super(P2D, self).__init__(data, distributor)
        self.prefix = 'P2D'

    def writer(self):
        pass
