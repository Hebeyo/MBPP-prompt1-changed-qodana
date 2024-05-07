def check_value(dict, n):
    for value in dict.values():
        if value != n:
            return False
    return True
