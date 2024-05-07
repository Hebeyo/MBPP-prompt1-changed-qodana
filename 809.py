def check_smaller(test_tup1, test_tup2):
  return all(x > test_tup2[i] for i, x in enumerate(test_tup1))
