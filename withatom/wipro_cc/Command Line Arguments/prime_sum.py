# Write a program to accept 10 numbers through command line arguments and
# calculate the sum of prime numbers among them.

import sys

sum = 0
for i in list(map(int, sys.argv[1:])):
    if int(i) > 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            sum += i
    else:
        continue
print(sum)
