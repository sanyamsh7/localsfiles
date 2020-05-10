#  Write a program to reverse a given number and print.
#
# Example:1
# I/P: 1234
# O/P:4321
#
# Example:2
# I/P:1004
# O/P:4001

number = int(input())
while number != 0:
    print(number%10, end = "")
    number = number // 10
