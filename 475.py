def sort_counter(dict1):
    sort_counter = sorted(dict1.items(), key = lambda x: x[1], reverse = True)
    return sort_counter
