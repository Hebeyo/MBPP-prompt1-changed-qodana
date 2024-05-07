def index_minimum(test_list):
  min_val = min([i[1] for i in test_list])
  for i in test_list:
    if i[1] == min_val:
      return i[0]
