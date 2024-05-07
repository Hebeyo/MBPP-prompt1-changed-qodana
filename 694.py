def extract_unique(test_dict):
  res = []
  for val in test_dict.values():
    for ele in val:
      if ele not in res:
        res.append(ele)
  return sorted(res)
