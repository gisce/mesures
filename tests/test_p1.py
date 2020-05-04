import unittest
from mesures.p1 import P1
from mesures.p1d import P1D
from sample_data import get_sample_data

class TestF1(unittest.TestCase):

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
