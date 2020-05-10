# Write a program to accept a number from the user and check whether
# it’s prime or not. If user enters anything other than number,
# handle the exception and print an error message.
try:
    number = int(input("enter your input: "))
    if number > 1:
        for i in range(2, number):
            if number%i == 0:
                print("number is not prime")
                break
        else:
            print("number is prime")
    else:
        print('number is not prime.')
except ValueError:
    print("ERROR: enter a number only")
