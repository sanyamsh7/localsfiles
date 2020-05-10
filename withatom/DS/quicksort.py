# #QUICK SORT WITH LOMUTO PARTITION SCHEME
#
# def quicksort(A, lo, hi):
#     #print("inside quick function:.....")
#     if lo < hi :
#         #print("before partition")
#         p = partition(A, lo, hi)
#         quicksort(A, lo, p-1)  #for lower elements
#         quicksort(A, p + 1, hi) #for higher elements
#         #print("after 2 recursion calls")
#     #print("after quick if statements")
#     return A
#
# def partition(A, lo, hi):
#     pivot = A[hi]
#     #print("pivot:", pivot)
#     i = lo
#     #print("i before loop--", i)
#     for j in range(lo, hi +1):
#         #print("j is:", j)
#         #print("array A:", A)
#         if A[j] < pivot:
#             #print("inside if statement")
#             #print("A[i]:", A[i], "A[j]:", A[j])
#             #print("i before increment:", i)
#             A[i], A[j] = A[j], A[i]
#             #print("array after swap:", A)
#             i += 1
#             #print("i after increment:", i)
#     #print("swap: A[i]:", A[i], "A[hi]:", A[hi])
#     A[i], A[hi] = A[hi], A[i]
#     #print("final Array:", A)
#     #print("final i:", i)
#     return i
#
# A = [5,1,7,3,4,2,5]
# #A = [1,2,3,4,5,6,7,8,9]
# print(quicksort(A, 0, len(A) - 1))

"""implementing quicksort in double linked list"""
from DoubleLinkedList import *
def len_list(node):
    pass
def scanner(count, node):
    i = 1
    while i < count:
        node = node.next
        i += 1
    return node

def quick(N, first, last):
    low = scanner(first, N.head)
    high = scanner(last, N.tail)
    if first < last:
        p = partition(A, low, high)

def partition(N, low, high):
    pivot = scanner(high, n.head)
    node = scanner(low, n.head)
    j = node
    for i in range(low - 1, high):
        if node.data < pivot.data:
            j.next, node.data = node.data, j.next
            j = j.next
        node = node.next
    j.data,

def quick_sort(numbers):
    quick(numbers, 0, 7)



numbers = DoubleLinkedList()
numbers.push(6)
numbers.push(1)
numbers.push(7)
numbers.push(3)
numbers.push(4)
numbers.push(2)
numbers.push(5)
#print("scanned element", scanner(1, numbers.head))
# node = numbers.head
# for i in range(0, 8):
#     print(node)
#     if node.next == None:
#         continue
#     node = node.next
