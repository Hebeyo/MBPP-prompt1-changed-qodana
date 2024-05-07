def most_occurrences(test_list):
  temp = {}
  for sub in test_list:
    for wrd in sub.split():
      if wrd in temp:
        temp[wrd] += 1
      else:
        temp[wrd] = 1
  max = 0
  for k, v in temp.items():
    if v > max:
      max = v
      res = k
  return (str(res))
