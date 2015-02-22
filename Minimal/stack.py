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
        ''' Inserts 'value' as a new node in the top of the stack. The min
        field in each node is updated so that you store the minimum value
        between the new node and all the nodes below '''
        newnode = Node(value)
        if self.size == 0:
            self.top = newnode
            newnode.min = value
        else:
            newnode.min = min(self.top.min, value)
            newnode.next = self.top
            self.top = newnode
        self.size += 1

    def min(self):
        ''' Returns the minimum value in the stack in O(1). '''
        return self.top.min

    def invert(self):
        new_stack = Stack()
        while not self.is_empty():
            element = self.pop()
            new_stack.push(element.value)

        self.top = new_stack.top

    def inverted_copy(self):
        new_stack = Stack()
        node = self.top
        while node is not None:
            new_stack.push(node.value)
            node = node.next
        return new_stack

    def sort(self):
    	aux = Stack()
    	while not self.is_empty():
    		element = self.pop()
    		while not aux.is_empty() and aux.top.value > element.value:
    			aux_element = aux.pop()
    			self.push(aux_element.value)
    		aux.push(element.value)
    	self.top = aux.top
    	self.size = aux.size


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
    s = Stack()
    for i in range(10, -1, -1):
        s.push(i)

    print s
    s.sort()
    print s
