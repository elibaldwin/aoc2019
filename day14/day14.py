
with open("input.txt") as f:
   lines = [x.strip().split(" => ") for x in f.readlines()]

from collections import defaultdict
needs = {}

for line in lines:
   req = line[0]
   created = line[1]
   created = created.split(" ")
   num = int(created[0])
   created = created[1]
   reqs = set()
   for x in req.split(", "):
      x = x.split(" ")
      reqs.add((int(x[0]), x[1]))
   needs[created] = (num, reqs)

import math
def num_ore(root, q):
   global needs
   needed = defaultdict(int)
   needed[root] = q
   while any(x != 'ORE' and needed[x] > 0 for x in needed):
      a = [x for x in needed if x != 'ORE' and needed[x] > 0][0]
      req = needs[a]
      given = req[0]
      num = math.ceil(needed[a] / given)
      req = req[1]
      needed[a] -= given * num
      for r in req:
         needed[r[1]] += r[0] * num
   return needed['ORE']


print("Part 1:", num_ore('FUEL', 1))

goal = 1000000000000

f = 1
amt = num_ore('FUEL', f)
while(amt < goal):
   f *= 2
   amt = num_ore('FUEL', f)

h = f
l = f // 2
while h - l > 2:
   m = l + ((h - l) // 2)
   amt = num_ore('FUEL', m)
   if amt > goal:
      h = m
   elif amt < goal:
      l = m
   else:
      print("found", m)
print("Part 2:", m)