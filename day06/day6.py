with open("day06/input.txt") as f:
  pairs = [x.strip().split(')') for x in f.readlines()]

from collections import defaultdict

orbits = defaultdict(list)
parents = {}

for pair in pairs:
  orbits[pair[0]].append(pair[1])
  parents[pair[1]] = pair[0]

def num_orbits(root, depth):
  total = depth
  for child in orbits[root]:
    total += num_orbits(child, depth+1)
  return total

print("Part 1:", num_orbits("COM", 0))

def shortest_path(start, end):
  global parents
  global orbits
  visited = set()

  queue = [start]

  dists = {}
  dists[start] = 0

  while True:
    curr = queue.pop(0)
    visited.add(curr)

    adj = orbits[curr]
    if curr in parents:
      adj.append(parents[curr])

    for a in adj:
      if a == end:
        return dists[curr] + 1

      if a not in visited:
        queue.append(a)
        dists[a] = dists[curr] + 1


start = parents["YOU"]
end = parents["SAN"]

print("Part 2:", shortest_path(start, end))


