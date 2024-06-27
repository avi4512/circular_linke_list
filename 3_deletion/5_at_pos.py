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

    def at_pos(self,pos,data):

        if pos == 1:
            np = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            np = Node(data)
            np.next = self.head
            temp.next = np
            self.head = np
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        np = Node(data)
        np.next = temp.next
        temp.next = np


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


cl.at_pos(3,25)

cl.display()



