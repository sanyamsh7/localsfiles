#Write a program to count the number of upper and lower case letters in a String.
string = "SaNyam SHaRma"
print("sample string:", string)
upper_count = 0
lower_count = 0
for i in string:
    if i.islower():
        lower_count += 1
    elif i.isupper():
        upper_count += 1
    else:
        continue

print("upper letters:", upper_count)
print("lower letters:", lower_count)
