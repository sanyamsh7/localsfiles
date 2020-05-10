#  Write a program to replace last value of tuples in a list to 100.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Sample list:", my_list)
index = 0
for i in my_list:
    l = list(i)
    l[2] = 100
    my_list[index] = tuple(l)
    index += 1

print("OUTPUT:", my_list)
