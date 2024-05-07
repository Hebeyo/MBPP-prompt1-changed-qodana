def round_and_sum(list1):
  round_and_sum=0
  for i in list1:
    round_and_sum+=round(i)
  round_and_sum=round_and_sum*len(list1)
  return round_and_sum
