#Write a program to print prime numbers between 10 and 99.
for i in range(10, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
