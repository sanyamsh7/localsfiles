from DoubleLinkedList import *

def bubbleSort(numbers):
    while True:
        #start with the second element
        node = numbers.head.next

        #start off assuming it is sorted
        is_sorted = True
        while node:
            if node.prev.data > node.data:
                #swap the nodes

                node.prev.data, node.data = node.data, node.prev.data
                #to loop again through the list
                is_sorted = False
            node = node.next
        #if it sorted then break the loop
        if is_sorted:
            break

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
