from mesures.p1 import P1

class P2(P1):
    def __init__(self, distributor, filepath):
        super(P2, self).__init__(distributor, filepath)
        self.prefix = 'P2'

    def writer(self):
        pass
