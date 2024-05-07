def check_abundant(n):
    sum = 0
    i = 1
    while i <= (n**0.5):
        if n%i == 0:
            if n/i == i:
                sum = sum + i
            else:
                sum = sum + i
                sum = sum + (n / i)
        i = i + 1
    sum = sum - n
    if sum > n:
        return True
    else:
        return False
