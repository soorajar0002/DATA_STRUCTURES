class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            return
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            print("STACK UNDERFLOW")
            return
        self.top = self.top.next

    def display(self):
        n = self.top
        while n:
            print(n.data, end=' ')
            n = n.next
        print("\n")


S = Stack()
S.push(3)
S.push(12)
S.push(43)
S.push(65)
S.push(84)

S.display()
S.pop()
S.pop()
S.display()