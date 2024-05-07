def find_k_product(test_list, K):
  res = 1
  for sub in test_list:
    res *= sub[K]
  return (res)
