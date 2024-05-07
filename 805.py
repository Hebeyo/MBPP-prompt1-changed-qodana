def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for list in lists:
        sum_list = sum(list)
        if sum_list > max_sum:
            max_sum = sum_list
            max_list = list
    return max_list
