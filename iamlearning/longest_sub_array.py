input1 = [13,15,12,18,18,14,5,12,13,32,33,5,1,93,75,25,11,9,77,78,79]
input2 = 21

sub_arrays = [[0]]

for i in range(input2):

    if input1[i]%2 != 0:
        if sub_arrays == [[0]]:
            sub_arrays[i][i] = input1[i]
        elif input1[i-1] == sub_arrays[-1][-1]:
            sub_arrays[-1].append(input1[i])
        else:
            sub_arrays.append([input1[i]])
arrays_len = [len(i) for i in sub_arrays]
print(max(arrays_len))
