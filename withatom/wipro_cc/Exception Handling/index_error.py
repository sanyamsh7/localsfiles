 # Declare a list with 10 integers and ask the user to enter an index.
 # Check whether the number in that index is positive or negative number.
 # If any invalid index is entered, handle the exception and print an error message.

my_list = [3, 2, -5, 1, 6, -7, 3, 7, 2, 8] # list of 10 random integers

index = int(input("enter the index: "))
try:
    if my_list[index] > 0:
        print("number at the index is positive")
    else:
        print("number at the index is negative")
except IndexError:
    print("ERRRO MESSAGE: Invalid index")
