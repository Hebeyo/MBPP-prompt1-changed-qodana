def check_type(test_tuple):
  if len(set(map(type, test_tuple))) == 1:
    return True
  return False
