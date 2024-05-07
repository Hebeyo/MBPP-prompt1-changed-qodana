def decode_list(alist):
    result = []
    for i in range(len(alist)):
        if isinstance(alist[i], list):
            result += [alist[i][1]] * alist[i][0]
        else:
            result.append(alist[i])
    return result
