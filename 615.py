def average_tuple(nums):
    result = []
    for i in range(len(nums[0])):
        result.append(sum([x[i] for x in nums]) / len(nums))
    return result
