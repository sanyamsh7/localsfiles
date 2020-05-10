# Given a string, if the first or last character is 'x', return the string without
#  those 'x' character, else return the string unchanged. If the input is "xHix",
#  then output is "Hi".
string = input("enter the string: ")
if string[0] == "x" and string[-1] == "x":
    print("stripped x:", string.strip("x"))
else:
    print("string unchanged:", string)
