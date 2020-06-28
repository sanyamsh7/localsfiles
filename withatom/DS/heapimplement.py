# implementing a HEAP #
from math import floor

def parent(A, i):
    """returns the index in A of the parent of i"""
    if i == 1:
        return None
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

array = [23, 5, 56, 23 , 7 ,8, 9, 3, 9]
print("sorted output",heap_sort(array))
