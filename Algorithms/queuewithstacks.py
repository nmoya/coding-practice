#!/usr/bin/python
import random
import stack


class QueueWithStacks():

    def __init__(self):
        ''' A queue that respects FIFO implemented with two stacks instead of
        a linked list. Stack B is responsible for dequeuing and Stack A for 
        enqueuing. '''
        self.stackA = stack.Stack()
        self.stackB = stack.Stack()
        self.size = 0

    def __repr__(self):
        _list = self.to_list()
        _list = map(str, _list)
        return ", ".join(_list)

    def to_list(self):
        invStack = self.stackA.inverted_copy()
        return self.stackB.to_list() + invStack.to_list()

    def is_empty(self):
        ''' Returns True if the queue is empty. False otherwise '''
        return self.size == 0

    def enqueue(self, value):
        ''' Insertions always occur in stackA '''
        self.stackA.push(value)
        self.size += 1

    def dequeue(self):
        ''' Removals always occur in StackB. If StackB is empty, all the
        content from StackA is moved to StackB '''
        if self.size == 0:
            return None
        else:
            if self.stackB.is_empty():
                while not self.stackA.is_empty():
                    element = self.stackA.pop()
                    self.stackB.push(element.value)

            element = self.stackB.pop()
            self.size -= 1
            return element


if __name__ == "__main__":
    q = QueueWithStacks()

    for i in range(10):
        q.enqueue(i)

    print q
    q.dequeue()
    q.enqueue(10)
    q.enqueue(11)
    print q

