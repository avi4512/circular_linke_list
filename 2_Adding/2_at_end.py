class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CricularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):

        if self.head is None:
            print("Circular Linked list is Empty...! ")
            return
        if self.head.next is None:
            print(self.head.data,'-->',end=" ")
            return
        temp = self.head.next
        print(self.head.data,'-->',end=" ")
        while temp != self.head:
            print(temp.data,'-->',end=" ")
            temp = temp.next
        print(temp.data)

    def at_end(self,data):

        if self.head is None:
            ne = Node(data)
            self.head = ne
            ne.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        ne = Node(data)
        ne.next = self.head
        temp.next = ne



cl = CricularLinkedList()

#Nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

#Connection
cl.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1

cl.at_end(45)

cl.display()



