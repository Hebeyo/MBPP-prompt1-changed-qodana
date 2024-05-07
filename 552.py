def Seq_Linear(seq_nums):
  diff = seq_nums[1] - seq_nums[0]
  for i in range(1, len(seq_nums) - 1):
    if seq_nums[i+1] - seq_nums[i] != diff:
      return "Non Linear Sequence"
  return "Linear Sequence"
