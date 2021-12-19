import unittest
from ejercicio6 import num_of_odd_sum

class test_num_odd_sum(unittest.TestCase):
    def test_basic1(self):
        self.assertEqual(num_of_odd_sum([1, 3, 5]), 4, "Debe ser igual a 4")
    def test_basic2(self):
        self.assertEqual(num_of_odd_sum([2, 4, 6]), 0, "Debe ser igual a 0")
    def test_zero(self):
        self.assertEqual(num_of_odd_sum([0, 0, 0]), 0, "Debe ser igual a 0")
    def test_empty(self):
        self.assertRaises(ValueError, num_of_odd_sum, [])
    def test_negative(self):
        self.assertRaises(ValueError, num_of_odd_sum, [-1, -1, -1])

if __name__ == "__main__":
    unittest.main()