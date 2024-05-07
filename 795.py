def cheap_items(items, n):
  import heapq
  return heapq.nsmallest(n, items, key=lambda s: s['price'])
