#sum square difference
#find the difference between the sum of the squares of the first one hundred natural numbers
#and the square of the sum of natural numbers
total_num = int(input())

sum_of_squares = (total_num*(total_num + 1)*(2*total_num + 1))//6
print(sum_of_squares)
sum_of_numbers = (total_num*(total_num + 1))//2
print(sum_of_numbers)
diff = sum_of_numbers**2 - sum_of_squares

print(diff)
