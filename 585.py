def expensive_items(items,n):
  expensive_items = sorted(items, key=lambda x: x['price'], reverse=True)
  return expensive_items[:n]
