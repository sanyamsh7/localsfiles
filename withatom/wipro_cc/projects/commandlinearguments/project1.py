# Through command line arguments three strings separated by space are given to
# you. Each string is a series of numbers separated by hyphen(-). You like all
# the numbers in string 1 and dislike all the numbers in string 2.
#
# Third string contains the numbers given to you. Your initial happiness is 0.
# When you encounter a number which is present in string 1, add 1 to your happiness,
# if it is present in string 2, add -1 to your happiness. Otherwise, your happiness
# does not change. Output your final happiness at the end.

import sys

script, string1, string2, string3 = sys.argv

numbers1 = list(map(int, string1.split("-")))
numbers2 = list(map(int, string2.split("-")))
numbers3 = list(map(int, string3.split("-")))

happiness = 0

for n in numbers3:
    if n in numbers1:
        happiness += 1

    elif n in numbers2:
        happiness += -1

    else:
        continue

print("happiness:", happiness)
