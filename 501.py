def num_comm_div(x, y):
    # Find the greatest common divisor between the two numbers
    gcd = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    # Find the number of common divisors
    result = 0
    for i in range(1, gcd + 1):
        if gcd % i == 0:
            result += 1
    return result
