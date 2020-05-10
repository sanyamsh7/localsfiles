#Write a program to accept two numbers as command line arguments and display their sum.
import sys

script, num1, num2 = sys.argv
numbers = list(map(int, sys.argv[1:]))
print("sum is: ", sum(numbers))
