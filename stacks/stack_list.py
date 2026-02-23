class Stack:
    def __init__(self):
        '''this function is constracter to the class Stack'''
        self.elements = []
        self.length = 0
    
    def push(self, data):
        '''this function append data to the stack list'''
        self.elements.append(data)
        self.length += 1
    