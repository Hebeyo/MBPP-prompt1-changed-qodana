def sum_even_odd(list1):
    even = False
    odd = False
    for i in list1:
        if i%2==0 and not even:
            even = i
        if i%2!=0 and not odd:
            odd = i
        if even and odd:
            return even+odd
    return -1
