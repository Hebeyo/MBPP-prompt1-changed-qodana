def ap_sum(a,n,d):
  total=0
  for i in range(n):
    total+=a
    a+=d
  return total
