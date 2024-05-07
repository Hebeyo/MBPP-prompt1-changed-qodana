def max_val(listval):
    max_val = 0
    for i in listval:
        if isinstance(i, int):
            if i > max_val:
                max_val = i
    return(max_val)
