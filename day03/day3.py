
with open("day03/input.txt") as f:
  wires = f.readlines()

wire1 = wires[0].split(',')

wire1 = [(x[0], int(x[1:])) for x in wire1]

moves = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

wire1grid = set()

wire1dists = dict()

pos = [0, 0]
wire1grid.add(tuple(pos))
steps = 0

for path in wire1:
  move = moves[path[0]]
  dist = path[1]
  for i in range(dist):
    pos[0] += move[0]
    pos[1] += move[1]
    steps += 1
    if (tuple(pos) not in wire1dists):
      wire1dists[tuple(pos)] = steps
    wire1grid.add(tuple(pos))
  

wire2 = wires[1].split(',')
wire2 = [(x[0], int(x[1:])) for x in wire2]

intersections = []
intersections2 = []

pos = [0, 0]
steps = 0
for path in wire2:
  move = moves[path[0]]
  dist = path[1]
  for i in range(dist):
    pos[0] += move[0]
    pos[1] += move[1]
    steps += 1
    if tuple(pos) in wire1grid:
      intersections.append(abs(pos[0]) + abs(pos[1]))
      intersections2.append(steps + wire1dists[tuple(pos)])


print("Part 1: ", min(intersections))
print("Part 2: ", min(intersections2))


      