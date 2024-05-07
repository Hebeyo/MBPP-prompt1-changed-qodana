def max_aggregate(stdata):
    temp = {}
    for name, marks in stdata:
        if name in temp:
            temp[name] += marks
        else:
            temp[name] = marks
    max_aggregate = max(temp.items(), key=lambda x: x[1])
    return max_aggregate
