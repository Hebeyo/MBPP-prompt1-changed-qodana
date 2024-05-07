def count_samepair(list1,list2,list3):
    result = 0
    for m,n,o in zip(list1,list2,list3):
        if m == n == o:
            result += 1
    return result
