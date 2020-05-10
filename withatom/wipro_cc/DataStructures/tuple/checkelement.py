#Write a program to check whether an element exists in a tuple or not.
my_tuple = (3,4,5,6,2,1)
print("existing tuple:", my_tuple)
element = int(input("enter the element: "))
if element in my_tuple:
    print(element, "exists in tuple.")
else:
    print(element, "does not exists.")
