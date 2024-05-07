from collections import Counter
def second_frequent(arr):
    count = Counter(arr)
    return sorted(count, key=count.get, reverse=True)[1]
