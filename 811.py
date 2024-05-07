def check_identical(test_list1, test_list2):
  for i in range(len(test_list1)):
    if test_list1[i] != test_list2[i]:
      return False
  return True
