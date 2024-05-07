def sum_of_square(n): 
    res = 1 
    for i in range(n + 1, 2 * n + 1): 
        res *= i 
    res1 = 1 
    for i in range(1, n + 1): 
        res1 *= i 
    return int(res / res1)
