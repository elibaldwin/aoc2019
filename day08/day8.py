with open("input.txt") as f:
  s = f.read().strip()

w = 25
h = 6

from collections import defaultdict
best = 999999999999
bestcounts = None
for i in range(100):
  count = defaultdict(int)
  for j in range(w*h):
    count[s[150*i + j]] += 1
  if (count['0']<best):
    best = count['0']
    bestcounts = count

print("Part 1", bestcounts['1'] * bestcounts['2'])

image = [['2' for _ in range(25)] for _ in range(6)]

transform = {'1': '#', '0': ' '}

for i in range(99, -1, -1):
  for x in range(h):
    for y in range(w):
      c = s[i * 150 + x * 25 + y]
      if c != '2':
        image[x][y] = transform[c]

print("Part 2:")
for line in image:
  print(''.join(line))
  

