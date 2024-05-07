def check_occurences(test_list):
  res = {}
  for ele in map(sorted, test_list):
    res[tuple(ele)] = res.get(tuple(ele), 0) + 1
  return res
