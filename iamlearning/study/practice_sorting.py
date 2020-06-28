# #practice merge sort
def merge_sort(A):
    length = len(A)
    if length == 1:
        return A
    mid = length//2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result

A = [3,4,2,6,1,7,4,34,21,6,2,6,2,7,8,89]
print(merge_sort(A))

# # practice insertion sort
def insertion_sort(A):
    for i in range(len(A)):
        key = A[i]
        pos = i
        while pos>0 and A[pos-1]>key:
            A[pos] = A[pos-1]
            pos -= 1
        A[pos] = key
    return A

A = [5,2,4,6,1,3,34,2,65,6,7,23,7546]

print(insertion_sort(A))
