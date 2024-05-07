def smallest_num(xs):
  min = xs[0]
  for i in xs:
    if i < min:
      min = i
  return min
