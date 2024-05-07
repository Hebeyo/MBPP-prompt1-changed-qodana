def min_product_tuple(list1):
    min_product = abs(list1[0][0] * list1[0][1])
    for x, y in list1:
        if abs(x*y) < min_product:
            min_product = abs(x*y)
    return min_product
