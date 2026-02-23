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