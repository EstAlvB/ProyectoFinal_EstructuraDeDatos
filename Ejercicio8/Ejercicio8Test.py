
from Ejercicio_8 import minInterval

import unittest

class TestMinInterval():
    def testValue1(self):
        intervals = [[2,3],[2,5],[1,8],[20,25]]
        queries = [2,19,5,22]
        A = minInterval(self, intervals, queries)
        self.assertEqual(minInterval(self, intervals, queries),A, "Deberia salir [2, -1, 4, 6] ")
    def testValue2(self):
        intervals = [[1,4],[2,4],[3,6],[4,4]]
        queries = [2,3,4,5]
        A = minInterval(self, intervals, queries)
        self.assertEqual(minInterval(self, intervals, queries),A, "Deberia salir [3, 3, 1, 4]")
    def testValue3(self):
        intervals = [[10,99],[2,4],[86,96],[10,11]]
        queries = [6,22,6,1]
        A = minInterval(self, intervals, queries)
        self.assertEqual(minInterval(self, intervals, queries),A, "Deberia salir [-1, 90, 90, -1]")
    def testValue4(self):
        intervals = [[65,89],[25,32],[8,95],[25,35]]
        queries = [65,32,16,81]
        A = minInterval(self, intervals, queries)
        self.assertEqual(minInterval(self, intervals, queries),A, "Deberia salir [25, 8, 88, 25]")
    def testValue5(self):
        intervals = [[223,4],[54,9],[114,223],[64,8]]
        queries = [15,54,3,2]
        A = minInterval(self, intervals, queries)
        self.assertEqual(minInterval(self, intervals, queries),A, "Deberia salir [5, 3, 3, 2]")

if __name__ == "__main__":
    unittest.main()