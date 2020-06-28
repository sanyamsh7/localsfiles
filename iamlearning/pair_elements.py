k = int(input())
array = [int(i) for i in input().split()]
pairs = []
length = len(array)
for i in range(length):
    for j in array[i+1:]:
        if (array[i] + j) == k:
            pairs.append(str((array[i], j)))

print("count: ", len(pairs), "pairs are", "".join(pairs))
