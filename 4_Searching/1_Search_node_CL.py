class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CricularLinkedList:

    def __init__(self):
        self.head = None


    def display(self):

        if self.head is None:
            print("Circular Linked list is Empty...! ")
            return
        if self.head.next == self.head:
            print(self.head.data,'-->',end=" ")
            return
        temp = self.head.next
        print(self.head.data,'-->',end=" ")
        while temp != self.head:
            print(temp.data,'-->',end=" ")
            temp = temp.next
        print(temp.data)

    def search(self,node):
        flag = 0
        if self.head is None:
            print("No Node is Present in the Linked list..")
            return
        if self.head.data == node:
            flag = 1
            print(node,'is Present at {}'.format(flag))
            return
        temp = self.head
        count = 1
        while temp.next != self.head:
            if temp.data == node:
                break
            count = count + 1
            temp = temp.next
        if temp.data == node:
            print(node,"is Present at {}".format((count)))
        else:
            print("Node was not found...")





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


cl.search(40)

cl.display()



