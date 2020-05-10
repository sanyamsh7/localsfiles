#  Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

number = int(input())
sum = 0

while number != 0:
    sum += number%10
    number = number // 10
print(sum)
