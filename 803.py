def is_Perfect_Square(n) :
    if n < 0:
        return False
    i = 1
    while i * i <= n:
        if n == i * i:
            return True
        i += 1
    return False
