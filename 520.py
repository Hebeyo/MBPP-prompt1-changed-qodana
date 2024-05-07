def get_lcm(l):
  l.sort()
  lcm = l[-1]
  while True:
    count = 0
    for i in l:
      if lcm % i == 0:
        count += 1
    if count == len(l):
      return lcm
    lcm += 1
