class Node():
    def __init__(self,a):
        self.a=a
        self.forward=None

class List():
    def __init__(self,node):
        self.head=node
        #self.head.forward=None
        self.next=None
        self.tail=self.head

    def add(self,node):
        #node.forward=self.tail
        #self.tail=node
        self.tail.next=node
        self.tail=self.tail.next
        self.tail.next=None

    def printf(self):
        p=self.head
        while(p!=None):
            print(p.a)
            p=p.next
        self.dequeue()

    def dequeue(self):
        self.head=self.head.next

node1=Node(10)
node2=Node(20)
list1=List(node1)
headp=list1.head
print('!',headp.a)
list1.add(node2)
list1.printf()
print(list1.head.a)
list1.printf()
print(headp.a)
