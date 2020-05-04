from mesures.p1 import P1

class P1D(P1):
    def __init__(self, data):
        super(P1D, self).__init__(data)
        self.prefix = 'P1D'

    def writer(self):
        pass