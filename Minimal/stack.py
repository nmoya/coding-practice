#!/usr/bin/python


class Node():

    def __init__(self, value):
    	''' Each node contains an integer, the minimum value for all nodes
    	below itself and a pointer to the next node '''
        self.value = value
        self.min = None
        self.next = None


class Stack():

    def __init__(self):
    	''' A stack object keeps a pointer to its top and manages the number
    	of elements in the stack '''
        self.top = None
        self.size = 0

    def __repr__(self):
    	return ", ".join(self.to_string())

    def is_empty(self):
    	''' Returns true if the stack is empty '''
    	return self.size == 0

    def to_list(self):
    	''' Inserts all the elements of the stack into a python list '''
    	curr = self.top
    	tmp = []
    	while curr is not None:
    		tmp.append(curr.value)
    		curr = curr.next
    	return tmp

    def to_string(self):
    	return map(str, self.to_list())

    def push(self, value):
    	''' Inserts 'value' as a new node in the top of the stack '''
        newnode = Node(value)
        if self.size == 0:
            self.top = newnode
            newnode.min = value
        else:
            newnode.min = min(self.top.min, value)
            newnode.next = self.top
            selt.top = newnode
        self.size += 1

    def pop(self):
    	''' Returns none if the stack is empty. Removes the node from the top
    	of the stack '''
    	if self.is_empty():
    		return None
    	else:
    		removed = self.top
    		self.top = self.top.next
    		self.size -= 1
    		return removed

if __name__ == "__main__":
	