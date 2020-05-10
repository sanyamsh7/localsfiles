# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def lastDigit(number1, number2):
    if ((number1 % 10) == (number2 % 10)):
        return True
    else:
        return False

print(lastDigit(7, 17))
print(lastDigit(6, 17))
print(lastDigit(3, 113))
