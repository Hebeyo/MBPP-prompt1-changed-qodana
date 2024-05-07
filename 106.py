def add_lists(test_list, test_tup):
  res = ()
  for i in test_tup:
    res += (i,)
  for i in test_list:
    res += (i,)
  return res
