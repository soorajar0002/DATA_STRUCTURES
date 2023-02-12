class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end =' ')
            current = current.next
            
    def evenOrOdd(self):
        current = self.head
        while current is not None:
            if current.data%2==0:
                print(current.data,"IS EVEN")
            else:
                print(current.data,"IS ODD")
            current = current.next
            
ll = LinkedList()
ll.add(5)
ll.add(3)
ll.add(4)
ll.add(1)
ll.add(87)
ll.display()
ll.evenOrOdd()