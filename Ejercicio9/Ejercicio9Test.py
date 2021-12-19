
from Ejercicio_9 import insertVal

import unittest

class TestInsertVal(unittest.TestCase):
    def testValue1(self):
        head = [3,4,1]
        value = 2
        A = insertVal(self,head, value)
        self.assertEqual(insertVal(head, value), A, "Deberia salir [3, 4, 1, 2] ")
    def testValue2(self):
        head = [1, 2, 3]
        value = 4
        A = insertVal(self,head, value)
        self.assertEqual(insertVal(head, value),A, "Deberia salir [1, 2, 3, 4] ")
    def testValue3(self):
        head = []
        value = 2
        A = insertVal(self,head, value)
        self.assertEqual(insertVal(head, value) , A, "Deberia salir [2] ")
    def testValue4(self):       
        head = [3,4,1]
        value = 0
        A = insertVal(self,head, value)
        self.assertEqual(insertVal(head, value) , A , "Deberia salir [3, 4, 0, 1] ")
    def testValue5(self):
        head = [32,54,18]
        value = 20
        A = insertVal(self,head, value)
        self.assertEqual(insertVal(head, value) , A , "Deberia salir [32, 54, 18, 20] ")
        
if __name__ == "__main__":
    unittest.main()