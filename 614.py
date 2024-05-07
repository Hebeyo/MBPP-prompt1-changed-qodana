def cummulative_sum(test_list):
  res = 0
  for i in range(len(test_list)):
    for j in range(len(test_list[i])):
      res += test_list[i][j]
  return (res)
