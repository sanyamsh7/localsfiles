#Write a function that takes a number as a parameter and checks whether the number is prime or not.

def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                return False
                break
        else:
            return True
    else:
        return f"number is not prime."
number = int(input("enter a number: "))
print(isprime(number))
