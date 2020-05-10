# Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(num, fact = 1):

    if num > 1:

        fact*= num
        return factorial(num-1, fact = fact)
    else:
        print(fact)

number = int(input())

factorial(number)
