#!/usr/bin/python
import random


def parent(k):
    return int(k / 2)


def children(k):
    return [2 * k, (2 * k) + 1]


class Heap():

    def __init__(self):
        self.elems = [0]
        self.N = 0

    def __repr__(self):
        tmp = []
        i = 1
        while i <= self.N:
            tmp.append(str(self.elems[i]))
            i += 1
        return " ".join(tmp)

    def move_up(self, k):
        father = parent(k)
        while k > 1 and (self.elems[father] < self.elems[k]):
            self.elems[father], self.elems[
                k] = self.elems[k], self.elems[father]
            k = parent(k)
            father = parent(k)

    def move_down(self, k):
        while 2 * k <= self.N:
            child = 2 * k
            if child < self.N and self.elems[child] < self.elems[child + 1]:
                child += 1
            if not self.elems[k] < self.elems[child]:
                break
            self.elems[k], self.elems[child] = self.elems[child], self.elems[k]
            k = child

    def insert(self, key):
        self.N += 1
        self.elems.append(key)
        self.move_up(self.N)

    def remove(self):
        value = self.elems[1]
        self.elems[1] = self.elems[self.N]
        self.elems[self.N] = None
        self.move_down(1)
        self.N -= 1
        return value


if __name__ == "__main__":

    h = Heap()

    for i in range(10):
        h.insert(random.randint(1, 10))

    print h

    for i in range(10):
        print h.remove()
