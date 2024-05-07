def find_max_val(n, x, y):
    max_val = -1
    for k in range(n + 1):
        if (k % x == y):
            max_val = max(max_val, k)
    return max_val
