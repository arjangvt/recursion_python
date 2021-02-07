"""
This code deletes k_th node from a linked list recursively

written by: Arjang Fahim
Last update: 2/5/2021

"""

# Stack last-in-first out

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self, data):
        self.root = Node(data)
        self.ptr = self.root

    def get_root(self):
        return self.root

    def get_ptr(self):
        return self.ptr
        
    def add_node(self, data):
        new = Node(data)
        self.ptr.next = new
        self.ptr = new
 
    def print_list(self):
        
        node = self.root

        while node != None:
            print(node.data)
            node = node.next

    def del_recursive(self, k, counter, n, prev):

        if n == None: return

        if k == 1: 
            
            self.root = self.root.next
            
            return

        if counter == k:
            prev.next = n.next
            return
        else:
            self.del_recursive(k, counter + 1, n.next, n)



    def del_by_index(self, k):
        
        if self.root == None: return

        counter = 1
        self.del_recursive(k, counter, self.root, self.root)





ll = LinkedList(1)
ll.add_node(2)
ll.add_node(10)
ll.add_node(100)
ll.add_node(1000)
ll.add_node(10000)

ll.print_list()
ll.del_by_index(6)
ll.print_list()