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

    def after_node(self,node,data):

        if self.head.data == node:
            an = Node(data)
            an.next = self.head.next
            self.head.next = an
            return
        temp = self.head
        while temp.next != self.head:
            if temp.data == node:
                break
            temp = temp.next
        if temp.next == self.head:
            print("Node was not Found...!")
        else:
            an = Node(data)
            an.next = temp.next
            temp.next = an


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

cl.after_node(30,45)

cl.display()



