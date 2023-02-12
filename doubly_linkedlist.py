class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
    
class Double_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            
            
    def display(self):
        current = self.head 
        if self.head == None:
            print("EMPTY")
            return
        while(current!=None):
            print(current.data,end= ' ')
            current=current.next

dll = Double_LL()
dll.add(1)
dll.add(2)
dll.add(3)
dll.add(4)
dll.add(5)
dll.display()