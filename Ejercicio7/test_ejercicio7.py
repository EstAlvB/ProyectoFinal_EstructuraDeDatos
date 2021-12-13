import unittest
from ejercicio7 import num_of_arths

class test_num_odd_sum(unittest.TestCase):
    def test_basic1(self):
        self.assertEqual(num_of_arths([2, 4, 6, 8, 10]), 7, "Debe ser igual a 7")
    def test_basic2(self):
        self.assertEqual(num_of_arths([7, 7, 7, 7, 7]), 16, "Debe ser igual a 16")
    def test_empty(self):
        self.assertRaises(ValueError, num_of_arths, [])
    def test_length(self):
        self.assertRaises(ValueError, num_of_arths, [0, 1])
    def test_negative(self):
        self.assertEqual(num_of_arths([-1, -1, -1, -1, -1]), 16, "Debe ser igual a 16")

if __name__ == "__main__":
    unittest.main()