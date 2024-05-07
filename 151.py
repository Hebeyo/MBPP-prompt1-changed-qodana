def is_coprime(x,y):
    if x == 1 or y == 1:
        return True
    for i in range(2,min(x,y)+1):
        if x % i == 0 and y % i == 0:
            return False
    return True
