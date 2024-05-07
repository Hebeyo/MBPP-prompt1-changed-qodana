def equilibrium_index(arr):
  for i in range(len(arr)):
    left_sum=0
    right_sum=0
    for j in range(i):
      left_sum+=arr[j]
    for j in range(i+1,len(arr)):
      right_sum+=arr[j]
    if left_sum==right_sum:
      return i
  return -1
