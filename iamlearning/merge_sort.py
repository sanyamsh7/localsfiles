#top-down approach
"""code below is for normal list of integers"""

def first(l):
    """returns first element of the list"""
    return l[0]

def rest(l):
    """returns rest of the element of the list"""
    return l[1:]

def merge_sort(list_m):
    """this function creates sublists of length 1"""
    if len(list_m) <= 1:
        #return list if only one or none element in list
        print('basecase:', list_m)
        return list_m

    left = []
    right = []
    for i, x in enumerate(list_m):
        #divide list in half
        if i < len(list_m)//2:
            print("left:", x)
            left.append(x)
        else:
            print("right", x)
            right.append(x)
    #recursive calls until sublists with one element are created
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    """merges the list in sorted order"""
    result = []
    print('merging')
    while left != [] and right != []:
        if first(left) <= first(right):
            result.append(first(left))
            print("left result:", result)
            left = rest(left)
            print("left", left)
        else:
            result.append(first(right))
            print("right result:", result)
            right = rest(right)
            print("right", right)
    while left != []:
        result.append(first(left))
        print("left while result", result)
        left = rest(left)
        print("left while ", left)
    while right != []:
        result.append(first(right))
        print("right while result", result)
        right = rest(right)
        print("right while:", right)
    return result

merge_sort([6,1,2,4,5,3,7,0])
