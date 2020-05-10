# Given a string and an integer n, return a string made of n repetitions of
# the last n characters of the string. You may assume that n is between 0 and the
#  length of the string inclusive. For example if the inputs are “Wipro” and 3,
#   then the output should be “propropro”.

string = input("enter the string: ")
integer = int(input("enter the integer: "))
length = len(string)
new_string = ""
if integer < length:
    for i in range(integer):
        new_string += string[-integer:]

print("string repetitions: ", new_string)
