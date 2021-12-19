from Ejercicio_3 import duplicado

import unittest

class TestDuplicado(unittest.TestCase):
    
    #Espacio de prueba
    def testValue1(self):
        #self = 0
        lista = [1,3,4,2,2]
        x =duplicado(self, lista)
        self.assertEqual(x, 2, "Deberia ser 2")
    def testValue2(self):
        #self = 0
        lista2 = [3,1,3,4,2]
        self.assertEqual(duplicado(self, lista2), 3,"Deberia ser 3")
    def testValue3(self):
        #self = 0
        lista3 = [1,1]
        x =duplicado(self, lista3)
        self.assertEqual(x, 1)

    def testValue4(self):
        #self = 0
        lista4 = [1,1,2]
        x =duplicado(self, lista4)
        self.assertEqual(x, 1)

    def testValue5(self):
        #self = 0
        lista5 = [1,4,4,2,3]
        x =duplicado(self, lista5)
        self.assertEqual(x, 4)


if __name__ == "__main__":
    unittest.main()