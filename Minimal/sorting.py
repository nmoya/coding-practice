#!/usr/bin/python
import random


def isSorted(array):
    ''' Checks if the array is sorted. An array is sorted if :
        pass for all i, a[i] < a[j]. Complexity: O(n) '''
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i + 1]:
            return False
        i += 1
    return True


def shuffle(array):
    ''' The numbers before i are shuffled. For each i, select another position
    of the array and swap with i. Complexity: O(n). '''
    i = 0
    while i < len(array):
        j = random.randrange(0, len(array))
        array[i], array[j] = array[j], array[i]
        i += 1


def merge(array, aux, lo, mid, hi):
    ''' Merge procedure called inside mergesort. Given a sorted left and
    right array, merge both arrays in a new array of size 
    len(left) + len(right) '''
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
    ''' Recursive function that splits the array in half each call and
    recursively sorts each half.'''
    if hi <= lo:
        return
    else:
        mid = (lo + hi) / 2
        _mergesort(array, aux, lo, mid)
        _mergesort(array, aux, mid + 1, hi)
        merge(array, aux, lo, mid, hi)


def mergesort(array):
    ''' Just the interface to call _mergesort. Mergesort is O(n log n) time and
    O(n) space. '''
    aux = [0 for i in range(len(array))]
    _mergesort(array, aux, 0, len(array) - 1)


def insertionsort(array):
    ''' All the numbers before i are sorted. For each i, traverse with j from 
    i + 1 until the end. If j < i, swap. That's it. Complexity: O(n^2). '''
    i = 0
    while i < len(array) - 1:
        j = i + 1
        while j < len(array):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
            j += 1
        i += 1


def selectionsort(array):
    ''' Very similar to insertionsort. All the numbers before i are sorted. 
    For each i, traverse with j from i + 1 until the end searching for the 
    minimum value. Swap the minimum value with i only once at the end.
    Complexity O(n^2). Usually worst than insertionsort. '''
    i = 0
    while i < len(array) - 1:
        _min, _min_pos = array[i + 1], i + 1
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
