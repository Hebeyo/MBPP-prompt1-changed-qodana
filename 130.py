def max_occurrences(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    max_key = max(dict, key=dict.get)
    return (max_key, dict[max_key])
