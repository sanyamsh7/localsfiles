# Write a program to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

print('available dictionaries:', dic1, dic2, dic3)
l_dict = [dic1, dic2, dic3]
new_dict = dict()
for d in l_dict:
    new_dict.update(d)
print("new dictionary:", new_dict)
