billions_list = [1_000_000_000, 100_000_000, 10_000_000, 1_000_000,
                    100_000, 10_000, 1_000, 100, 10, 1]

array = list(map(int, input().split()))
list_len = len(array)
number = 0

for i in range(-1, -list_len -1, -1):
        number += array[i] * billions_list[i]

number += 1

print(list(map(int, str(number))))
