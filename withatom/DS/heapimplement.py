# implementing a HEAP #
from math import floor
from sys import exit

def parent(i):
    """returns the index in A of the parent of i"""
    if i <= 0:
        return None
    if i == 2:
        return 0
    return floor(i/2)

def left(A, i):
    """returns the index in A of the left child of i"""
    if 2*i +1  < len(A):
        return 2*i +1  # the left child index should be in A.len
    else:
        return None

def right(A, i):
    """returns the index in A of the right child of i"""
    if 2*i + 2 < len(A):
        return 2*i + 2
    else:
        return None

def max_heapify(A, i, n):
    """modifies A so that i roots a heap"""

    lft = left(A, i)
    rght = right(A, i)
    if lft == None or rght == None:
        return None
    if lft < n and A[lft] > A[i]:
        largest = lft
    else:
        largest = i
    if rght < n and A[rght] > A[largest]:
        # there was a typo in pseudocode at A[r] < A[largest],
        # above condition is the correction
        largest = rght
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)

def build_max_heap(A):
    """returns A modified to represent heap"""
    n = len(A)
    for i in range(len(A)//2 -1,-1, -1):
        max_heapify(A, i, n)

def heap_sort(A):
    """returns modified A sorted from smallest to largest"""
    build_max_heap(A)
    print("heap", A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, 0, i)
    return A

def heap_increase_key(A, i, key):
    """ A still representing a heap where the key of A[i] was increased to key"""
    if i >= len(A) or i < 0:
        print("ERROR: NONE node at this index")
        exit(1)

    if key <= A[i] :
        print("ERROR: new key must be greater than current key")
        exit(1)

    A[i] = key
    # for maintaining heap
    while i > 0  and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)



array = [23, 5, 56, 23 , 7 ,8, 9, 3, 9]
# print("sorted output",heap_sort(array))
build_max_heap(array)
print(array)
heap_increase_key(array,4, 100)
print(array)
print("sorted output",heap_sort(array))
