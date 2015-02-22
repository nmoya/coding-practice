#!/usr/bin/python
import random
import linkedlist


class Queue():

    def __init__(self):
        ''' A queue holds a pointer to a list. The elements are inserted at the
        end and removed from the front. (FIFO). '''
        self.start = linkedlist.List()
        self.size = 0

    def __repr__(self):
        _list = self.start.to_string()
        return ", ".join(_list)

    def is_empty(self):
        ''' Returns True if the queue is empty. False otherwise '''
        return self.size == 0

    def enqueue(self, value):
        ''' Insert a node with 'value' at the end of the list '''
        self.start.insert(value)

    def dequeue(self):
        ''' Removes the first element from the queue '''
        



   


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
