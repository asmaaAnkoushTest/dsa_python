class Queue:
    def __init__(self):
        '''this function is constructor to the class Queue'''
        self.elements = []
        self.length = 0

    def enqueue(self, data):
        '''this function add data to the end'''
        #Time Complexity O(1)
        #Space complexity O(1)
        self.elements.append(data)
        self.length += 1
    
