#!/usr/bin/python
import random


def binary_search(array, key):
    lo = 0
    hi = len(array)-1

    while lo <= hi:
        mid = (lo + hi) / 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            hi = mid-1
        else:
            lo = mid+1
    return False


def is_sorted(array):
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


def merge(array, lo, mid, hi):
    ''' Merge procedure called inside mergesort. Given a sorted left and
    right array, merge both arrays in a new array of size 
    len(left) + len(right) '''
    left = array[lo:mid+1]
    right = array[mid+1:hi+1]

    k = lo
    i = j = 0
    while i < len(left) or j < len(right):
        if i >= len(left):
            array[k] = right[j]
            j+=1
        elif j >= len(right):
            array[k] = left[i]
            i+=1
        elif left[i] <= right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k += 1


def _mergesort(array, lo, hi):
    ''' Recursive function that splits the array in half each call and
    recursively sorts each half.'''
    if lo < hi:
        mid = (hi + lo) / 2
        _mergesort(array, lo, mid)
        _mergesort(array, mid+1, hi)
        merge(array, lo, mid, hi)


def mergesort(array):
    ''' Just the interface to call _mergesort. Mergesort is O(n log n) time and
    O(n) space. '''
    _mergesort(array, 0, len(array)-1)


def insertionsort(array):
    ''' All the numbers before i are sorted. For each i, traverse with j from 
    i until the 0. If the current a[j] < a[j-1], swap. Complexity: O(n^2). '''
    i = 0
    while i < len(array):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
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


def partition(array, lo, hi):
    pivot = array[hi]
    i = lo - 1 
    j = lo
    while j <= hi-1:
        if array[j] <= pivot:
            i += 1;
            array[i], array[j] = array[j], array[i]
        j += 1
    array[i+1], array[hi] = array[hi], array[i+1]
    return (i + 1)


def _quicksort(array, lo, hi):
    if lo < hi:
        pivot = partition(array, lo, hi)
        _quicksort(array, lo, pivot - 1)
        _quicksort(array, pivot + 1, hi)


def quicksort(array):
    _quicksort(array, 0, len(array) - 1)


if __name__ == "__main__":
    tmp = []
    for i in range(1000):
        tmp.append(random.randint(0, 100))

    mergesort(tmp)
    print is_sorted(tmp)
    print binary_search(tmp, 32), 32 in tmp
    # shuffle(tmp)
    # print is_sorted(tmp)
    # quicksort(tmp)
    # print is_sorted(tmp)
