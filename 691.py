def group_element(test_list):
  res = dict()
  test_list = sorted(test_list, key = lambda ele: ele[1])
  for ele in test_list:
    if ele[1] in res:
      res[ele[1]].append(ele[0])
    else:
      res[ele[1]] = [ele[0]]
  return res
