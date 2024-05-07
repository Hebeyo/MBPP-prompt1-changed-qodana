def max_of_nth(test_list, N):
  max = test_list[0][N]
  for i in test_list:
    if i[N] > max:
      max = i[N]
  return (max)
