# Write a program to accept two numbers from the user and perform division.
# If any exception occurs, print an error message or else print the result.

try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = 0
    result = num1/num2
except :
    print("Exception occurred")
else:
    print("result:",result)
