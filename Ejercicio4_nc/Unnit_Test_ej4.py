from MissingRolls import MissingRolls

import unittest
class TestMissingRolls(unittest.TestCase):
    def test1(self):
        self.assertEqual(MissingRolls([1], 3, 1), [5])

    def test2(self):
        self.assertEqual(MissingRolls([3,2,4,3], 4, 2), [6,6])

    def test3(self):
        self.assertEqual(MissingRolls([1,5,6], 3, 4), [2,2,2,3])

    def test4(self):
        self.assertRaises(ValueError,MissingRolls,[1,3,5],3,0)

    def test5(self):
        self.assertRaises(ValueError, MissingRolls, [1, 3, 5], 0, 4)







if __name__ == '__main__':

    unittest.main()