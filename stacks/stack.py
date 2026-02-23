class Node:
    def __init__(self, value):
        '''this function is constracter to the class Node'''
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        '''this function is constracter to the class Stack'''
        self.top = -1
        self.length = 0

    def push(self, data):
        '''this function add data in the top of stack: node point to old top and then updata top'''
        node: Node = Node (data)
        node.next = self.top
        self.top = node
        self.length += 1
