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
    assert (isSorted(array[lo:mid+1]))
    assert (isSorted(array[mid+1:hi+1]))

    k = lo
    while k <= hi:
        aux[k] = array[k]
        k += 1

    k = lo
    i = lo
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

if __name__ == "__main__":
    tmp = []
    for i in range(10):
        tmp.append(random.randint(0, 100))

    mergesort(tmp)
    print isSorted(tmp), tmp
    shuffle(tmp)
    print isSorted(tmp), tmp
    mergesort(tmp)
    print isSorted(tmp)

