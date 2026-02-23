from linked_lists.linked_list import LinkedList

class Stack:
    def __init__(self):
        '''this function is constructor to the class Stack'''
        self.elments: LinkedList = LinkedList()
    
    def push(self, data):
        '''this function append_end data to the stack linked list'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        self.elments.append_end(data)
    
    def pop(self):
        '''this function return and delete the last element in stack'''
        #Time Complexity is O(n).
        #Space complexity is o(1).
        return self.elments.remove_at(self.elments.length-1)

