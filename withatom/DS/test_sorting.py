# import bubblesort
# import mergesort
import sorting
from DoubleLinkedList import *
from random import randint
max_numbers = 800

def random_list(count):
    numbers = DoubleLinkedList()
    # numbers.shift(2)
    # numbers.shift(1)
    # numbers.push(3)
    node = numbers.head
    for i in range(count, 0, -1):
        numbers.push(randint(0,1000))
        #numbers.shift(2)
    return numbers

def is_sorted(numbers):
    node = numbers.head
    while node and node.next:
        if node.data > node.next.data:
            return False
        else:
            node = node.next
    return True

def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubbleSort(numbers)
    #assert is_sorted(numbers)
    return numbers

def test_merge_sort():
    numbers = random_list(max_numbers)
    sorting.merge_sort(numbers)
    assert is_sorted(numbers)

# def test_quick_sort():
#     numbers = random_list(mar_numbers)
#     quicksort.quick_sort(numbers)
#     assert is_sorted(numbers)

# def print_list(numbers):
#     node = numbers.head
#     while node and node.next:
#         print(node)
#         node = node.next

test_bubble_sort()
test_merge_sort()
