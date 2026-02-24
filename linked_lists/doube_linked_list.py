class Node:
    def __init__(self, value):
        '''this function is constructor to the class Node'''
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        '''this function is constructor to the class Double Linked List'''
        self.head = None
        self.length = 0
        