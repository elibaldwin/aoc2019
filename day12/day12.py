with open("input.txt") as f:
  ps = [x.strip().replace("<", "").replace(">", "").split(", ") for x in f.readlines()]
  ps = [[int(y[2:]) for y in x] for x in ps]

def abssum(triple):
  return sum([abs(x) for x in triple])

vs = [[0 for _ in range(3)] for _ in range(4)]

def grav(p1, p2, v1, v2):
  for i in range(3):
    if p1[i] == p2[i]:
      continue
    elif p1[i] > p2[i]:
      v1[i] -= 1
      v2[i] += 1
    else:
      v2[i] -= 1
      v1[i] += 1

def move(p, v):
  for i in range(3):
    p[i] += v[i]

def printmoon(p, v):
  print(f"pos=<x={p[0]}, y={p[1]}, z={p[2]}>, vel=<x={v[0]}, y={v[1]}, z={v[2]}>")

def total_energy(ps, vs):
  return sum([abssum(x[0])*abssum(x[1]) for x in zip(ps, vs)])

axis = set()
m = 10

axis = 0


import math

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

part1 = False

axes = []
for axis in range(3):
  init = (tuple([p[axis] for p in ps]), tuple([v[axis] for v in vs]))
  for step in range(1000000000):
    if step == 1000 and not part1:
      print("Part 1:", total_energy(ps, vs))
      part1 = True
    for i in range(4):
      for j in range(i+1, 4):
        grav(ps[i], ps[j], vs[i], vs[j])
    for i in range(4):
      move(ps[i], vs[i])
    if (tuple([p[axis] for p in ps]), tuple([v[axis] for v in vs])) == init:
      break
  axes.append(step+1)


print("Part 2:", lcm(lcm(axes[0], axes[1]), axes[2]))





  