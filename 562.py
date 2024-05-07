def Find_Max_Length(lst):  
    maxLength = 0
    for x in lst:
        if len(x) > maxLength:
            maxLength = len(x)
    return maxLength
