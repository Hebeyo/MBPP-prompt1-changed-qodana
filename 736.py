def left_insertion(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
