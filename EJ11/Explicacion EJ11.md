# Expliacion EJ 11
## Strobogrammatic Numbers

mi solucion funciona de la siguiente forma, solo podemos usar cierto numero de chars que son strobogramaticos, (180 grados ==) por lo tanto podemos solo buscar todas las permutaciones de un lado del numero y "dar la vuelta" al otro lado y unir como str.

si es que el numero es par entonces solo dividimos el numeor en dos y buscamos todas las permutaciones de ese tamaño.

si es impar realizamos lo mismo pero obtenemos los tres numero simetricos solo (no 6 o 9) y los ponemos en el medio, por lo que obtenemos 3 veces mas que si nos saltaramos este paso. 

la funcion reveerse primero transforma los 6 en 9 y viceversa y luego devuelve en forma de string pero en sentido contrario usando indexing [::-1]

la complejidad de esta es forma de resolver es de $O(N^3 + N)$ porque la funcion product() de itertoos es basicamente un doble laso, mas en el que esta y el de reverse.