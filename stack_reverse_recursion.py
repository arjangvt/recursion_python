"""
This code reverse a content of a stack by using ADT stack functions recursively.

written by: Arjang Fahim
Last update: 2/6/2021

"""

# Stack last-in-first out

class Stack:

    def __init__(self):
        self.s = []
        self.ptr = 0


    def isEmpty(self):
        if len(self.s) == 0:    # or if end == 0 
            return True
        return False

    def push(self, item):
        self.s.append(item)
        self.ptr = self.ptr + 1

        
    def pop(self):
        #if (self.is_empty) 
        #    return 
        self.ptr = self.ptr - 1
        item = self.s.pop(self.ptr)

        return item

    def print_stack(self):
        print (self.s)

    
    def InsertItem(self, item):

        if self.isEmpty():
            self.push(item)
            
        else:   
            temp = self.pop()
            self.InsertItem(item)
            self.push(temp)
            

    def reverse_stack(self):

        if not self.isEmpty():
            
            item = self.pop()
            self.reverse_stack()
            print(item)

            self.InsertItem(item)
            

        return





            

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()

s.reverse_stack()
s.print_stack()