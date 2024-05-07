def unique_product(list_data):
    p = 1
    for i in list(set(list_data)):
        p *= i
    return p
