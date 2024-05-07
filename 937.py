def max_char(str1):
    temp = {}
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    max_char = max(temp, key = temp.get)
    return max_char
