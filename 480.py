def get_max_occuring_char(str1):
  max = 0
  ch = ''
  for i in str1:
    if str1.count(i) > max:
      max = str1.count(i)
      ch = i
  return ch
