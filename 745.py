def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        num = str(i)
        if '0' in num:
            continue
        divisible = True
        for digit in num:
            if i % int(digit) != 0:
                divisible = False
                break
        if divisible:
            result.append(i)
    return result
