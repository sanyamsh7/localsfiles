#  Write a program to find if the given number is palindrome or not
#
# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.
#
# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.

number = int(input())
reverse = ""
n = number
while n != 0:
    reverse += str(n%10)
    n = n//10

if int(reverse) == number:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome")
