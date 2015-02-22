#!/usr/bin/python
import random


class Node():

    def __init__(self, value):
        ''' A node is composed of a pointer to the next node and an integer '''
        self.next = None
        self.value = value


class List():

    def __init__(self):
        ''' A list holds a pointer to the first and last node. It also
        keeps track of its size '''
        self.first = None
        self.last = None
        self.size = 0

    def __repr__(self):
        _list = self.to_string()
        return ", ".join(_list)

    def to_list(self):
        ''' Converts from the List class to a python built in list. The
        elements are mapped as integers. '''
        _list = []
        curr = self.first
        while curr is not None:
            _list.append(curr.value)
            curr = curr.next
        return _list

    def to_string(self):
        ''' Converts from the List class to a python built in list. The
        elements are mapped as strings. '''
        _list = self.to_list()
        _list = map(str, _list)
        return _list

    def is_empty(self):
        ''' Returns true if the list is empty. False otherwise '''
        return self.size == 0

    def insert_ordered(self, value):
        ''' Insert a node with 'value' in an ordered list '''
        if self.is_empty():
            self.insert(value)
        else:
            newnode = Node(value)
            if value <= self.first.value:
                curr = self.first
                self.first = newnode
                newnode.next = curr
            elif value >= self.last.value:
                self.last.next = newnode
                self.last = newnode
            else:
                previous, curr = None, self.first
                while curr.value < value:
                    previous = curr
                    curr = curr.next

                previous.next = newnode
                newnode.next = curr
            self.size += 1

    def insert(self, value):
        ''' Insert a node with 'value' at the end of the queue '''
        newnode = Node(value)
        if self.is_empty():
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.size += 1

    def remove(self, value):
        ''' Removes and return the node with the value. Returns None if
                the value does not exhist '''
        previous, curr = None, self.first
        while curr is not None and curr.value != value:
            previous = curr
            curr = curr.next

        if curr is None:
            return None
        else:
            self.size -= 1
            previous.next = curr.next
        return curr

    def remove_duplicates(self):
        ''' Removes all values with frequency > 1 leaving only one node '''
        curr = self.first
        while curr is not None:
            previous = curr
            runner = curr.next
            while runner is not None:
                if runner.value == curr.value:
                    previous.next = runner.next
                    self.size -= 1
                    if self.last == runner:
                        self.last = previous
                runner = runner.next
            curr = curr.next

    def reverse(self, node, previous=None):
        ''' Reverses a list in-place '''
        if node is None:
            aux = self.last
            self.last = self.first
            self.first = aux
            return
        else:
            self.reverse(node.next, node)
            node.next = previous


if __name__ == "__main__":
    l = List()
    for i in range(5):
        l.insert(i)

    l.remove(3)
    l.remove(7)

    l = List()
    for i in range(10):
        l.insert_ordered(random.randint(0, 100))

    print l
    l.reverse(l.first)
    print l

    l = List()
    l.insert(1)
    l.insert(1)
    l.insert(2)
    l.insert(2)
    l.insert(3)
    l.insert(3)
    l.insert(3)
    l.remove_duplicates()
    print l
