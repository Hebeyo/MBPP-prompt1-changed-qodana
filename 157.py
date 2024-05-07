def encode_list(list1):
    result = []
    count = 1
    for i in range(1, len(list1)):
        if list1[i] == list1[i - 1]:
            count += 1
        else:
            result.append([count, list1[i - 1]])
            count = 1
    result.append([count, list1[-1]])
    return result
