#Write a program to check if a given key already exists in a dictionary.
dic1 = {2:34, 3: 45, 4:56}
print('existing dictionary:', dic1)

key = int(input())
print('key:', key)

if key in dic1.keys():
    print("key exists in dictionary.")
else:
    print("key doesnot exists in dictionary.")
