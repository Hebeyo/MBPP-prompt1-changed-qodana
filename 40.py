def freq_element(nums):
  result = {}
  for i in nums:
    for j in i:
      if j in result:
        result[j]+=1
      else:
        result[j]=1
  return result
