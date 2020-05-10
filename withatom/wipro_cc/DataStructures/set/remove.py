#Write a program to remove a given item from the set.

my_set = {"hi", "hello", "ola", "namastey"}
print("sample set:", my_set)
item = input("enter your element: ")
if item in my_set:
    my_set.remove(item)
    print("set after modification:", my_set)
else:
    print("item not in set.")
