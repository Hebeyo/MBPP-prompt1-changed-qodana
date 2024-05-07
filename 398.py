def sum_of_digits(nums):
  sum = 0
  for n in nums:
    for el in str(n):
      if el.isdigit():
        sum += int(el)
  return sum
