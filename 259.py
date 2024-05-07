def maximize_elements(test_tup1, test_tup2):
  res = []
  for tup1, tup2 in zip(test_tup1, test_tup2):
    temp = []
    for a, b in zip(tup1, tup2):
      if a > b:
        temp.append(a)
      else:
        temp.append(b)
    res.append(tuple(temp))
  return tuple(res)
