from Quadratic_function import sortArray

import unittest
class TestQuadraticFunction(unittest.TestCase):
    def test1(self):
        x=sortArray([-4,-2,2,4],A=1,B=3,C=5)
        self.assertListEqual(x,[3,9,15,33])

    def test2(self):
        y = sortArray([0, 0, 0, 0], A=1, B=3, C=5)
        self.assertListEqual(y, [5, 5, 5, 5])

    def test3(self):
        z = sortArray([2, 1, 3, 4], A=0, B=0, C=0)
        self.assertListEqual(z, [0, 0, 0,0])

    def test4(self):
        w = sortArray([-4, -2, 2, 4], A=-1, B=3, C=5)
        self.assertListEqual(w, [-23, -5, 1, 7])

    def test5(self):
        v = sortArray([-1, -1, -1, -1], A=-1, B=-1, C=-1)
        self.assertListEqual(v, [-1, -1, -1, -1])


if __name__ == '__main__':

    unittest.main()

