
# string = input()
# encoded_string = ""
# count = 1
# j = 0
#
# for i in range(len(string)):
#     letter = string[i]
#     if encoded_string == "":
#         encoded_string += letter
#     elif letter == encoded_string[j]:
#         count += 1
#     else:
#         encoded_string += str(count)
#         encoded_string += letter
#         j += 2
#         count = 1
#
# if letter == encoded_string[-1]:
#     encoded_string += str(count)
#
# print(encoded_string)

# ....using dictionary.....
d = dict()
string = input()
for i in string:
    if i not in d.keys():
        d.update({i: 1})
    else:
        d[i] += 1

#create string of d
letters = list(d.keys())
integers = list(d.values())
for i,j in zip(letters,integers):
    print(i, j, end = "", sep = "")
