#implementing bubble sort
# def swap(i, j, Arr):
#     Arr[i], Arr[j] = Arr[j], Arr[i]
#
# def bubbleSort(Arr):
#     n = len(Arr)
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(1, n):
#             #if this pair is out of order
#             if Arr[i-1] > Arr[i]:
#                 swap(i-1, i, Arr)
#                 swapped = True
#     return Arr
# print(bubbleSort([6,1,5,2,3]))


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
