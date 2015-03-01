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

    def to_list(self):
        return self.start.to_list()

    def is_empty(self):
        ''' Returns True if the queue is empty. False otherwise '''
        return self.size == 0

    def enqueue(self, value):
        ''' Insert a node with 'value' at the end of the list '''
        self.start.append(value)
        self.size += 1

    def dequeue(self):
        ''' Removes the first element from the queue '''
        self.size -= 1
        return self.start.remove_first()


if __name__ == "__main__":
    q = Queue()

    for i in range(10):
        q.enqueue(i)
    print q

    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q
