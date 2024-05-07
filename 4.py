def heap_queue_largest(nums, n):
    import heapq as hq
    hq.heapify(nums)
    largest_nums = hq.nlargest(n, nums)
    return largest_nums
