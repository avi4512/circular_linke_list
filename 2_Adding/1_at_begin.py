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

    def at_begin(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
            return
        nb = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = nb
        nb.next = self.head
        self.head = nb




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

cl.at_begin(5)

cl.display()



