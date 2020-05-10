#  Given a string, return a new string made of n copies of the first 2 chars of
#  the original string where n is the length of the string. The string length will be >=2.
# If input is "Wipro" then output should be "WiWiWiWiWi".

string = input("enter the string: ")

new_string = ""

for i in range(len(string)):
    new_string += string[:2]

print("new_string:", new_string)
