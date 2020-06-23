#even fibonacci numbers sum

##first, second = 1,2 
##nxt = 0
##n = 100
##s = 0
##while second<4000000:
##    nxt = first +second
##    if second%2==0:
##        s += second
##    first = second
##    second = nxt
##
##print(s)

#efficient
#in fibo seq every third element is even
#so only the third number is added
#1 1 2 3 5 8 13 21 34 55 89 144....
limit = 4000000
s = 0
a = 1
b =1
c = a+b
while c <limit:
    s += c
    a = b+c
    b = c+a
    c = a+b

print(s)
