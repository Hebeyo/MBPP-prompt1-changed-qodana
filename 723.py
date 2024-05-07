def count_same_pair(nums1, nums2):
    result = sum([1 for i in range(len(nums1)) if nums1[i] == nums2[i]])
    return result
