## Andres Martinez

##Insertion sort program

from itertools import product

def findStr(n):
    
    """
    solo se debe hacer una permutacion de los numeros de la mitad del tamaño y 
    luego repetirla del otro lado (cambio 6 y 9)
    """
    output = []
    posChars = ["0","1","6","8","9"]
    symetricC = ["0","1","8"]
    
    def reverse (Strobo_num):
        str = ''
        for i in Strobo_num:
            if i == "6":
                str = str + "9"
            elif i == "9":
                str = str + "6"
            else:
                str = str + i
        return str[::-1]
    
    if n < 0: raise ValueError ("int is a negative number")
    if n is not int: raise TypeError ("number of strobogrammatic numbers not an int")
    if n == 0: return [""] 
    if n == 1: return ["1", "0", "8"]
    
    if (n % 2 == 0):
        #par, solo copiamos las combinaciones al reves
        for i in product(posChars,repeat = n//2):
            str = ''.join(i)
            output.append(str + reverse(i))
        
    if (n % 2 != 0):
        #impar, unimos las combinaciones con cada uno de los symetricC en el medio
        
        for j in symetricC:
            for i in product(posChars,repeat= n//2): #redondea auto a min
                str = ''.join(i)
                output.append(str + j + reverse(i))
    
    return output
