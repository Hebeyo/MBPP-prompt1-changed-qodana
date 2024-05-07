def sort_list(test_list):
  test_list.sort(key = lambda x: sum([len(str(ele)) for ele in x]))
  return (str(test_list))
