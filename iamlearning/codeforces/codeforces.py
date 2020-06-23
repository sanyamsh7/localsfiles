inputs = [int(i) for i in input().split()]
percent = inputs[2]/100
completion = percent * inputs[0]

k = [int(i) for i in str(completion).split(".")]
ith = int((k[1]*inputs[1])/100)
for i in range(1, inputs[0]+1):
    if i <= k[0]:
        print(inputs[1], end = " ")
    elif i==k[0]+1:
        print(ith, end = " ")
    else:
        print(0, end = " ")
