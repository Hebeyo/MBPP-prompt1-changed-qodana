def mul_even_odd(list1):
    even = False
    odd = False
    for i in list1:
        if i%2==0 and even==False:
            even = True
            even_num = i
        elif i%2!=0 and odd==False:
            odd = True
            odd_num = i
    return even_num*odd_num
