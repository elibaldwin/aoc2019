
with open("input.txt") as f:
  field = [x.strip() for x in f.readlines()]

from collections import defaultdict
import math

blocked = defaultdict(set)
asteroids = set()

for y in range(len(field)):
  for x in range(len(field[y])):
    if field[y][x] == '#':
      asteroids.add((x, y))

def find_blocked():
  global blocked, asteroids
  for a in asteroids:
    blocked[a].add(a)
    for b in asteroids:
      if a != b and b not in blocked[a]:
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        bx = b[0]
        by = b[1]
        g = math.gcd(dx, dy)
        dx = int(dx / g)
        dy = int(dy / g)
        while 0 <= bx <= 24 and 0 <= by <= 24:
          bx += dx
          by += dy
          if (bx, by) in asteroids:
            blocked[a].add((bx, by))
            blocked[(bx, by)].add(a)

def find_best(blocked, asteroids):
  best = 0
  best_a = None
  counts = {}
  for k,v in blocked.items():
    seen = asteroids - v
    s = len(seen)
    counts[k] = s
    if s > best:
      best = s
      best_a = k
  return (best, best_a)

find_blocked()
best, best_a = find_best(blocked, asteroids)
print("Part 1:", best)

def get_order(a, visible):
  order = []
  for a in visible:
    dx = a[0] - best_a[0]
    dy = a[1] - best_a[1]
    angle = (math.degrees(math.atan2(dx, -dy)) + 360) % 360
    order.append((angle, a))
  order.sort()
  return order

tbd = asteroids - blocked[best_a]
order = get_order(best_a, tbd)

asteroids.remove(best_a)

count = 0
while len(asteroids) > 0:
  for _, a in order:
    asteroids.remove(a)
    count += 1
    if(count == 200):
      print("Part 2:", a[0] * 100 + a[1])
  blocked = defaultdict(set)
  find_blocked()
  tbd = asteroids - blocked[best_a]
  order = get_order(best_a, tbd)