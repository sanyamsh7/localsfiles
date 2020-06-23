#simple solution
#going through all the numbers from 1 to target
##s = 0
##for i in range(1, 100000000):
##    if i%3==0 or i%5==0:
##        s += i
##print(s)

#more efficient solution :
#divibles of 3 +divisibles of 5 -divisibles of 15
#for 3 --> target//3 (999//3==333)
#for 5 --> target//5 (995/5 similar to 999//5==199(round to nearest integer)
#also, sum of series 1+2+3.....+n == half*n*(n11)
#for 3 --> 3+6+9... 999 == 3*(1+2+3+4..333)
#for 5 --> 5+10+15... 995==5(1+2+3...199)
#eq. becomes 3*(target//3*(target//3 + 1)/2

target = 1000
def sum_divisible(n):
    p = (target-1)//n   #999//n
    eq = n*(p*(p+1))//2
    return eq
s = (sum_divisible(3) + sum_divisible(5)) - sum_divisible(15)
print(s)
