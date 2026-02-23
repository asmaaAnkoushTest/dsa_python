class Node:
    def __init__(self, value):
        '''this function is constructor to the class Node'''
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        '''this function is constructor to the class Queue'''
        self.head = None
        self.tail = None
        self.length: int = 0

    def enqueue(self, data):
        '''this function add data to the end'''
        #Time Complexity O(1)
        #Space complexity O(1)
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def __str__(self):
        '''this function for human-readable representation'''
        #Time Complexity O(n)
        #Space complexity O(1)
        current_head = self.head
        string: str = "head "
        while current_head:
            string = string + " -> "
            string = string + f"{current_head.value}"
            current_head = current_head.next
        string = string + " <- tail"
        return string


