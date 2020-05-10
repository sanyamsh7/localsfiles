#Write a program to find the index of an item in a tuple.
my_tuple = (3,2,5,1,6,9)
print("sample tuple:", my_tuple)
item = int(input("enter your item: "))
if item in my_tuple:
    print("index of item specified:", my_tuple.index(item))
else:
    print("item does not exists in tuple.")
