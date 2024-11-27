class Node:

    __slots__ = ['value', 'next']

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next

class Stack:

    __slots__ = ['Top','Size']

    def __init__(self) -> None:
        self.Top = None
        self.Size = 0

    def isEmpty(self):
        return self.Size == 0
    
    def get_size(self):
        return self.Size
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.Top
        self.Top = newNode
        self.Size += 1

    def pop(self):
        deletedNode = self.Top.value
        self.Top = self.Top.next
        self.Size -= 1
        return deletedNode
    