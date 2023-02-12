class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            print("EMPTY")
            return

        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display(self):
        n = self.front
        if self.front is None:
            print("Empty")
            return
        while n:
            print(n.data, end=" ")
            n = n.next
        print("\n")


q = Queue()
q.enqueue(10)
q.enqueue(32)
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.display()
q.dequeue()

q.display()
