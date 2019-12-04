with open("practice/aoc2015/day3/input.txt") as f:
  directions = f.read().strip()

moves = {'>': (1, 0), '^': (0, 1), '<': (-1, 0), 'v': (0, -1)}

pos = [0, 0]

seen = set()
seen.add(tuple(pos))

for d in directions:
  move = moves[d]
  pos[0] += move[0]
  pos[1] += move[1]
  seen.add(tuple(pos))

print(len(seen))

pos = [[0, 0], [0, 0]]
seen = set()
seen.add((0,0))

for i in range(0, len(directions), 2):
  for j in range(2):
    d = directions[i+j]
    move = moves[d]
    pos[j][0] += move[0]
    pos[j][1] += move[1]
    seen.add(tuple(pos[j]))
  
print(len(seen))