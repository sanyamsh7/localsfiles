##alarm clock
t = int(input())
for i in range(t):
    a,b,c,d = map(int, input().split())
    if a<=b:
        print(b)
        continue
    if c<=d:
        print(-1)
        continue
    x = (a-b + 1)//(c-d)
    print(b + x*c)

