# Explicacion EJ 2
## RandomizedSet

a pesar de lo que diga el nombre, no se puede realizar este ejercicio usando un hash-set en tiempo constante, debido a que la ultima operacion es un getRandom(). si quisieramos obtener un getRandom() con un set tendriamos que pasarlo a una lista primero, lo que toma $O(n)$.

la solucion que uso es con dos hash-maps sincornizados y un contador de elementos, el primer hash-map usa el numero de index como key y el valor como valor, el otro toma el valor como key y el index como valor. la idea es que se puedan buscar indexes de valores y valores de indexes en tiempo constante.

el contador de valores solo lo necesitamos para el getRandom, solo sacamos un valor entre 0 y el numero de elementos y obtenemos el valor del hash-map de indexes.

para insert() solo añadimos a los dos hash-map los index y los valor en sus respectivos lugares

para el remove() tenemos que sacar un valor de los dos, para lo que primero obtenemos el index usando el valor, luego retirarmos el valor del hash-map de indexes con un .pop(). el problema es que ahora tenemos un hueco en los hash-maps por lo que ponemos los ultimos valores en el lugar del anterior, y asi no tenemos que mover todo el hash-map de ninguno. primero movemos el valor del ultimo al lugar del anterior (linea 38), luego en el otro hash-map ponemos el valor del ultimo usando el index que guardamos antes, y por ultimo eliminamos el otro ultimo valor.