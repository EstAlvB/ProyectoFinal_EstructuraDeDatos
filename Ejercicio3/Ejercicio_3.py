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

