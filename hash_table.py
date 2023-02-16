class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        
        
class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
        
    def hash_function(self,key):
        return sum(ord(c) for c in key)% self.size
    
    def set(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key,value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        
    def get(self,key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(key)
table = HashTable(10)

# add some key-value pairs to the table
table.set("apple", 1)
table.set("banana", 2)
table.set("cherry", 3)

# retrieve values from the table using keys
print(table.get("apple"))  # output: 1
print(table.get("banana"))  # output: 2
print(table.get("cherry"))  # output: 3

# update values in the table
table.set("banana", 4)
print(table.get("banana"))  # output: 4