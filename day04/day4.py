A = "278384-824795"
A = range(278384, 824795+1)

def fits_criteria(test):
  test = str(test)
  prev = test[0]
  count = 1
  counts = []
  for c in test[1:]:
    if c == prev:
      count+=1
    else:
      counts.append(count)
      count = 1
    if int(c) < int(prev):
      return (False, False)
    prev = c
  counts.append(count)
  return (max(counts) >= 2, 2 in counts)

s1 = 0
s2 = 0
for i in A:
  result = fits_criteria(i)
  if result[0]:
    s1+=1
  if result[1]:
    s2+=1
  

print("Part 1:", s1)
print("Part 2:", s2)