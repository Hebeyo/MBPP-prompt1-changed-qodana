def pack_consecutive_duplicates(list1):
    result = []
    temp = []
    for i in range(len(list1)):
        if i == 0:
            temp.append(list1[i])
        elif list1[i] == list1[i-1]:
            temp.append(list1[i])
        else:
            result.append(temp)
            temp = [list1[i]]
    result.append(temp)
    return result
