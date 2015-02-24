#!/usr/bin/python
import random


def isSorted(array):
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i + 1]:
            return False
        i += 1
    return True


def shuffle(array):
  i = 0
  while i < len(array):
      j = random.randrange(0, len(array))
      array[i], array[j] = array[j], array[i]
      i += 1

def merge(array, aux, lo, mid, hi):
    k = lo
    while k <= hi:
        aux[k] = array[k]
        k += 1

    k = i = lo
    j = mid + 1
    while k <= hi:
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > hi:
            array[k] = aux[i]
            i += 1
        elif aux[j] <= aux[i]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1
        k += 1

def _mergesort(array, aux, lo, hi):
    if hi <= lo:
        return
    else:
        mid = (lo + hi) / 2
        _mergesort(array, aux, lo, mid)
        _mergesort(array, aux, mid + 1, hi)
        merge(array, aux, lo, mid, hi)


def mergesort(array):
    aux = [0 for i in range(len(array))]
    _mergesort(array, aux, 0, len(array) - 1)


def insertionsort(array):
    i = 0
    while i < len(array) - 1:
        j = i + 1
        while j < len(array):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
            j += 1
        i += 1

def selectionsort(array):
    i = 0
    while i < len(array) - 1:
        _min, _min_pos = array[i+1], i+1
        j = i + 2
        while j < len(array):
            if array[j] < _min:
                _min = array[j]
                _min_pos = j
            j += 1
        array[i], array[_min_pos] = _min, array[i]
        i += 1


if __name__ == "__main__":
    tmp = []
    for i in range(1000):
        tmp.append(random.randint(0, 100))

    selectionsort(tmp)
    print isSorted(tmp)
    shuffle(tmp)
    print isSorted(tmp)
    selectionsort(tmp)
    print isSorted(tmp)

