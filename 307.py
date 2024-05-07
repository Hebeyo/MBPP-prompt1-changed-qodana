def colon_tuplex(tuplex,m,n):
  tuplex = list(tuplex)
  tuplex[m].append(n)
  return tuple(tuplex)
