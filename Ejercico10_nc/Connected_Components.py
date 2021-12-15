#10. You have a graph of $n$ nodes. You are given an integer $n$
#and an array edges where edges[i] = [ai, bi] indicates that there
#is an edge between ai and bi in the graph
#Return the num of connected componets in the graph


class ConectedComponents:

    def __init__(self, v):
        # vertices
        self.v = v
        # arreglo con lista enlazada
        self.linkedlist = [[] for i in range(self.v)]

    # agrega un edge
    def addEdge(self, v1, v2):

        self.linkedlist[v1].append(v2)
        self.linkedlist[v2].append(v1)
        if v1 == v2:
            ValueError("Los valores de los nodos no pueden ser iguales")

    # esta sera la funcion que nos retornara
    #el numero de conexiones
    def num_connected_components(self):
        #emepezamos con los vertices marcados como no visitados
        visited = [False for i in range(self.v)]
        #contador de conexiones
        counter = 0
        for i in range(self.v):
            if (visited[i] == False):
                self.dfs(i, visited)
                counter += 1
        return counter
#aquí usamos la estructura dfs para recorrer nuestros nodos
    def dfs(self, v, visited):
        #se marca el nodo en el que esté, como visitado
        visited[v] = True

        #recorre los vertices que estes juntos a este vertice
        for i in self.linkedlist[v]:
            if visited[i]== False:
                self.dfs(i, visited)
