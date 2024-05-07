def nth_items(list,n):
  return [list[i] for i in range(len(list)) if i%n==0]
