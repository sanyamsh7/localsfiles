# Write a function that accepts a string and prints the number of upper case
# letters and lower case letters in it.

def count_s(string):
    upper = 0
    lower = 0
    for i in string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        else:
            continue
    return f"UPPER: {upper} , LOWER: {lower}"

string = input('enter the string: ')
print(count_s(string))
