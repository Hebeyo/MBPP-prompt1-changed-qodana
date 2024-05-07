def two_unique_nums(nums):
  res = []
  for i in nums:
    if nums.count(i) == 1:
      res.append(i)
  return res
