def large_product(nums1, nums2, N):
    result = [x*y for x in nums1 for y in nums2]
    result.sort(reverse=True)
    return result[:N]
