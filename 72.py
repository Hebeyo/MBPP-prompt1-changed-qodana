def dif_Square(n):
    for i in range(2, n):
        for j in range(2, n):
            if i*i - j*j == n:
                return True
    return False
