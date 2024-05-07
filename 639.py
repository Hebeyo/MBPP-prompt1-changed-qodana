def sample_nam(sample_names):
  n=0
  for name in sample_names:
    if name[0].isupper() and name[1:].islower():
      n+=len(name)
  return n
