def digit_sum(number):
    sum = 0
    if number < 0:
        number = -(number)
        sum = cal_sum(number)
        return -(sum)
    else:
        return cal_sum(number)
    

def cal_sum(number):
    sum = 0
    while number != 0:
            sum += number % 10
            number = number // 10
            if number == 0 and sum//10 != 0:
                number = sum
                sum = 0
    return sum

print(digit_sum(-2345))
