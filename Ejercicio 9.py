 #Ejercicio 9 

 #Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into 
 # the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list 
 # and may not necessarily be the smallest value in the circular list.
#If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, 
# the circular list should remain sorted.

#If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference 
# to that single node. Otherwise, you should return the originally given node.

#Creamos el nodo
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

#Definimos la funcion              
def insertVal(self, head, value):
    if not head:
        nNode = Node(value, None)
        nNode.next = nNode
        return nNode
    oHead = head
    while(head):
        if(head.next.val > head.val):
            if(value >= head.val) and (value <= head.next.val):
                break
        elif(head.next.val < head.val):
            if(value >= head.val) or (value <= head.next.value):
                break
        elif(head.next == oHead):
            break
        head = head.next
    head.next = Node(value, head.next)
    return head
    
#Espacios de prueba
def testValue1():
    self = 0
    head = [3,4,1]
    value = 2
    A = insertVal(self,head, value)
    assert insertVal(head, value) == A, "Deberia salir [3, 4, 1, 2] "
def testValue2():
    self = 0
    head = [1, 2, 3]
    value = 4
    A = insertVal(self,head, value)
    assert insertVal(head, value) == A, "Deberia salir [1, 2, 3, 4] "
def testValue3():
    self = 0
    head = []
    value = 2
    A = insertVal(self,head, value)
    assert insertVal(head, value) == A, "Deberia salir [2] "
def testValue4():
    self = 0
    head = [3,4,1]
    value = 0
    A = insertVal(self,head, value)
    assert insertVal(head, value) == A, "Deberia salir [3, 4, 0, 1] "
def testValue5():
    self = 0
    head = [32,54,18]
    value = 20
    A = insertVal(self,head, value)
    assert insertVal(head, value) == A, "Deberia salir [32, 54, 18, 20] "
    
def main():
    testValue1()
    testValue2()
    testValue3()
    testValue4()
    testValue5()
if __name__ == "__main__":
    main()
