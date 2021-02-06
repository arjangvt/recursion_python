"""
This code sorts a stack only with ADT functions recursively.

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

    
    def insert_item(self, item):

        if self.isEmpty():
            self.push(item)
            
        else:

            temp = self.pop()
            if temp > item:
                self.insert_item(item)
                self.push(temp)
            else:
                self.insert_item(temp)
                self.push(item)
            

    def sort_stack(self):

        if not self.isEmpty():
            item = self.pop()
            self.sort_stack()
            self.insert_item(item)  
        return





            

s = Stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.print_stack()

s.sort_stack()
s.print_stack()