#Write a program to iterate over a dictionary using for loop and
#print the keys alone, values alone and both keys and values.
my_dict = {2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
keys = []
values = []
key_value = []
for key,value in my_dict.items():
    keys.append(key)
    values.append(value)
    key_value.append({key:value})

print("existing dictionary:", my_dict)
print("keys are:", keys)
print("values are:", values)
print("key-value pairs:", key_value)
