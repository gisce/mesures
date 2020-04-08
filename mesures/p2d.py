from mesures.p2 import P2

class P2D(P2):
    def __init__(self, distributor, filepath):
        super(P2D, self).__init__(distributor, filepath)
        self.prefix = 'P2D'

    def writer(self):
        pass
