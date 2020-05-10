# #top-down approach
# """code below is for normal list of integers"""
#
# def first(l):
#     """returns first element of the list"""
#     return l[0]
#
# def rest(l):
#     """returns rest of the element of the list"""
#     return l[1:]
#
# def merge_sort(list_m):
#     """this function creates sublists of length 1"""
#     if len(list_m) <= 1:
#         #return list if only one or none element in list
#         return list_m
#
#     left = []
#     right = []
#     for i, x in enumerate(list_m):
#         #divide list in half
#         if i < len(list_m)//2:
#             left.append(x)
#         else:
#             right.append(x)
#     #recursive calls until sublists with one element are created
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
#
# def merge(left, right):
#     """merges the list in sorted order"""
#     result = []
#     while left != [] and right != []:
#         if first(left) <= first(right):
#             result.append(first(left))
#             left = rest(left)
#         else:
#             result.append(first(right))
#             right = rest(right)
#     while left != []:
#         result.append(first(left))
#         left = rest(left)
#     while right != []:
#         result.append(first(right))
#         right = rest(right)
#     return result

"""implementing merge_sort for doubly linked list"""
from DoubleLinkedList import *

def count(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count

def first(node):
    # print("first---", node)
    return node.data

def rest(node):
    # print("rest---", node.next)
    return node.next

def sublists(left, right, node):
    # print("inside sublists")
    mid = node
    i = 0
    len = count(node)//2
    left = node     #head of the list
    for i in range(0, len - 1):
        mid = mid.next
    if mid.next == None:
        right = mid
    else:
        right = mid.next
        right.prev = None
    mid.next = None
    # print("left:---", left, "right:---", right)
    return (left, right)

def merge_sort(n):
    # print("mergesort")
    if type(n) == DoubleLinkedList:
        # print("type of n---", type(n))
        node = n.head
    else:
        # print("node n---", n)
        node = n
    if count(node) <= 1:
        return node

    left = None
    right = None
    left, right = sublists(left, right, node)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    # print("merge")
    result = DoubleLinkedList()
    while left != None and right != None:
        if first(left) <= first(right):
            result.push(left.data)
            # print("result:---", result.head)
            left = rest(left)
        else:
            result.push(right.data)
            # print("result:---", result.head)
            right = rest(right)

    while left != None:
        result.push(left.data)
        # print("result:---", result.head)
        left = rest(left)

    while right != None:
        result.push(right.data)
        #print("result:---", result.head)
        right = rest(right)

    return result.head
#
# numbers = DoubleLinkedList()
# numbers.push(6)
# numbers.push(1)
# numbers.push(2)
# numbers.push(4)
# numbers.push(5)
# numbers.push(7)
# numbers.push(3)
# numbers.push(8)
# numbers.push(9)
#
# node = numbers.head
# for i in range(8, 0, -1):
#     print(node)
#     node = node.next
# # print(first(numbers.head))
# # print(sublists(None, None, numbers.head))
# result = merge_sort(numbers)
# for i in range(8, 0 , -1):
#     print(result, end = ' ')
#     result = result.next
# print()
