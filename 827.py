def sum_column(list1, C):
    result = 0
    for row in list1:
        result += row[C]
    return result
