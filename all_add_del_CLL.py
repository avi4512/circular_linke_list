class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_linkedlist:

    def __init__(self):
        self.head = None

    def display(self):

        if self.head is None:
            print("Circular Linked list is Empty...!")
            return

        print(self.head.data,"-->",end=" ")
        temp = self.head.next
        while temp != self.head:
            print(temp.data,"-->",end=" ")
            temp = temp.next
        print(temp.data)

    def add_at_begin(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
            nb.next = self.head
            return
        temp = self.head
        nb = Node(data)
        while temp.next != self.head:
            temp = temp.next
        temp.next = nb
        nb.next = self.head
        self.head = nb

    def add_at_end(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
            nb.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        ne = Node(data)
        ne.next = temp.next
        temp.next = ne

    def add_at_pos(self,pos,data):

        if pos == 0:
            np = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = np
            np.next = self.head
            self.head = np
            return

        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np = Node(data)
        np.next = temp.next
        temp.next = np

    def del_at_begin(self):

        if self.head is None:
            print("Can't remove from Empty Circular Linked list...!")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head

    def del_at_end(self):
        if self.head is None:
            print("Can't remove from Empty Circular Linked list...!")
            return
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    def del_at_pos(self,pos):

        if pos == 0:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
            return
        temp = self.head
        prev = None
        for i in range(pos-1):
            prev = temp
            temp = temp.next
        temp.next = temp.next.next

    def del_by_val(self,n):

        if self.head is None:
            print("Can't remove from Empty Linked list...!")
            return
        #val_at_Begin
        if self.head.data == n:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
            return
        #val_at_end
        temp = self.head
        prev = None
        while temp.next != self.head:
            if temp.data == n:
                break
            prev = temp
            temp = temp.next
        if temp.next == self.head:
            print("Element Not Found...!")
        else:
            prev.next = self.head


cll = Circular_linkedlist()

#Adding
#At_begib
cll.add_at_begin(30)
cll.add_at_begin(20)
cll.add_at_begin(25)
cll.add_at_begin(10)
#AT_END
cll.add_at_end(40)
#AT_POSITION
cll.add_at_pos(0,5)


#Deletion
#AT_BEGIN
cll.del_at_begin()
#AT_END
cll.del_at_end()
#AT_POS
cll.del_at_pos(1)
#By_val
cll.del_by_val(30)




cll.display()


