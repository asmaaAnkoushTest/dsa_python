class Node:
    def __init__(self, value):
        '''this function is constracter to the class Node'''
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        '''this function is constracter to the class Stack'''
        self.top = None
        self.length = 0

    def push(self, data):
        '''this function add data in the top of stack: node point to old top and then updata top'''
        #Time Complexity is O(1)
        node: Node = Node (data)
        node.next = self.top
        self.top = node
        self.length += 1
    
    def __str__(self):
        ''''this function for human-readable representation"'''
        current_top = self.top
        string: str = "\n"
        while current_top:
            string = string + f"{current_top.value}\n"
            string = string + "^\n"
            current_top = current_top.next
        return string

    def pop (self):
        ''''this function remove and return the top element in stack'''
        #Time Complexity is O(1)
        if self.top == None:
            raise IndexError ("The Stack is Empty")
        else:
            poped_data = self.top.value
            self.top = self.top.next
            self.length -= 1
            return poped_data
