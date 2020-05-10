#Write a program to check if a given number is prime or not.
number = int(input())

if number > 1:
    for i in range(2, number):
        if (number % i == 0):
            print(number, "is not a Prime")
            break
    else:
        print(number, "is a Prime Number")
else:
    print(number, "is not a Prime")
