def maximum_value(test_list):
  res = []
  for key, lst in test_list:
    res.append((key, max(lst)))
  return res
