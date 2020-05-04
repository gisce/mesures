import unittest
from mesures.f1 import F1
from sample_data import get_sample_data

class TestF1(unittest.TestCase):

    def test_gen_f1(self):
        data = get_sample_data()
        f = F1(data)
        f.writer()
        self.assertIsInstance(f, F1, 'F1 test fail')

if __name__ == '__main__':
    unittest.main()
