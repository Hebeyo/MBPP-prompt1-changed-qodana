def areEquivalent(num1,num2):
    sum1 = 1
    sum2 = 1
    for i in range(2, num1):
        if num1 % i == 0:
            sum1 += i
    for i in range(2, num2):
        if num2 % i == 0:
            sum2 += i
    return sum1 == sum2
