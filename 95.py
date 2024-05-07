def Find_Min_Length(lst):  
    minLength = len(lst[0])
    for i in lst:  
        if len(i) < minLength:  
            minLength = len(i) 
    return minLength
