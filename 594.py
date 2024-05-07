def diff_even_odd(list1):
    first_even = -1
    first_odd = -1
    for i in list1:
        if i%2==0:
            first_even = i
            break
    for i in list1:
        if i%2!=0:
            first_odd = i
            break
    return (first_even-first_odd)
