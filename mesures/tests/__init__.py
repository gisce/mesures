import unittest
from mesures.f1 import F1
from mesures.p1 import P1, P1D
from mesures.sample_data.data import get_sample_data

class TestF1(unittest.TestCase):

    def test_gen_f1(self):
        data = get_sample_data()
        f = F1(data)
        f.writer()
        self.assertIsInstance(f, F1, 'F1 test fail')

    def test_gen_p1(self):
        data = get_sample_data()
        f = P1(data)
        f.writer()
        self.assertIsInstance(f, P1, 'P1 test fail')

    def test_gen_p1d(self):
        data = get_sample_data()
        f = P1D(data)
        f.writer()
        self.assertIsInstance(f, P1D, 'P1D test fail')

if __name__ == '__main__':
    unittest.main()