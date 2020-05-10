 # Write a program to prepare a dictionary where the keys are numbers
 # between 1 and 15 (both included) and the values are square of the keys.

dict1 = dict()

for i in range(1, 16):
    dict1.update({i: i**2})

print('prepared dictionary:', dict1)
