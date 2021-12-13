#Ejercicio 3

#3. Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#- There is only one repeated number in nums, return this repeated number.
#- You must solve the problem without modifying the array nums and uses only constant extra space.

#Creamos la funcion
def duplicado(self, lista):
    if (len(lista) > 1):
        puntero1 = lista[0]
        puntero2 = lista[lista[0]]
        
        while puntero1 != puntero2:
            puntero1 = lista[puntero1]
            puntero2 = lista[lista[puntero2]]
        puntero2 = 0
        while puntero1 != puntero2:
            puntero1 = lista[puntero1]
            puntero2 = lista[puntero2]
        return puntero1
    if (len(lista) < 1):
        print("La lista esta vacia")
    return -1

#Espacio de prueba
def testValue1():
    self = 0
    lista = [1,3,4,2,2]
    assert duplicado(self, lista) == 2, "Debería salir 2"
def testValue2():
    self = 0
    lista2 = [3,1,3,4,2]
    assert duplicado(self, lista2) == 3, "Debería salir 3"
def testValue3():
    self = 0
    lista3 = [1,1]
    assert duplicado(self, lista3) == 1, "Debería salir 1"
def testValue4():
    self = 0
    lista4 = [1,1,2]
    assert duplicado(self, lista4) == 1, "Debería salir 1"
def testValue5():
    self = 0
    lista5 = [1,4,4,2,3]
    assert duplicado(self, lista5) == 4, "Debería salir 4"

def main():    
    testValue1()
    testValue2()
    testValue3()
    testValue4()
    testValue5()

if __name__ == "__main__":
    main()
    print("Todo salio bien")