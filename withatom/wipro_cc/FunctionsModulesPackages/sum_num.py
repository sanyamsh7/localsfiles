#  Write a function to return the sum of all numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def return_sum(lis1):
    sum = 0
    for i in lis1:
        sum += i
    return sum

sample = [8, 2, 3, 0, 7]
print("sample list:", sample)
print("returned sum:", return_sum(sample))
