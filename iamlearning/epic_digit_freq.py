
#number = "113344422222"  ### worst case(solution for this is line 20)
#number = "12323434455345" ###normal case
#number = "11111222223333344444"  #### this works because it is already sorted
number = "11111333334444422222"  ###worst case for condition at line20

### uncomment lines -- 8, 9 ,14 and commment line 15 for solution to all the cases.
list_digits = [int(i) for i in number]
list_digits.sort()

d = dict()
max = 0
greatest = 0
for i in list_digits:
#for i in number:
    if i in d:
        d[i] += 1
    else:
        d.update({i:1})
print(d)
for j in d.items():
    print(j)
    if max <= j[1]:
        max = j[1]
        print("max", max)
        if greatest < int(j[1]):   # here
            greatest = int((j[0]))
print(greatest)
