class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoubleLL:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"<--->",end = '')
                n = n.nref
    def reverse_traversal(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            if n.nref is None:
                print(n.data)
            else:
                while n.nref is not None:
                    n = n.nref
                while n.pref is not None:
                    print(n.data,"<--->",end='')
                    n = n.pref
    def insert_empty(self,data):
        if self.head is not None:
            print("Linked List is not Empty")
        else:
            new_node = Node(data)
            self.head = new_node
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Element is Not Present in the Linked list")
        else:
            n.nref.pref = new_node
            new_node.pref = n
            new_node.nref = n.nref
            n.nref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is Empty")
            return
        else:
            if self.head.nref is None:
                if self.head.data == x:
                    self.head.pref = new_node
                    new_node.nref = self.head
                    self.head = new_node
                    return
            n = self.head
            while n.nref is not None:
                if x == n.nref.data:
                    break
                n = n.nref
            if n is None:
                print("Element is not Present in the Linked List")
            else:
                new_node = Node(data)
                n.nref.pref = new_node
                new_node.pref = n
                new_node.nref = n.nref
                n.nref = new_node
    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = self.head.nref
            self.head.pref = None
    def delelte_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    def delete_by_value(self,data):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                print("Linked List is Empty after deletion")
            else:
                print("Element is not present in the Linked List")
        if self.head.data == x:
            self.head.nref.pref = None
            self.head = self.head.nef
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is None:
            print("Element is Not Present in the Linked List")
        else:
            n.nref.pref = n.pref
            n.pref.nref = n.nref

a = DoubleLL()
a.insert_empty(300)
a.add_begin(100)
a.add_end(500)
a.add_after(200,100)
a.add_before(400,500)
a.forward_traversal()



