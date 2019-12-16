from intcode import IntComputer

in_dir = 0
def f_dir():
   global in_dir
   return in_dir

# 1 = north, 2=south, 3=west, 4 = east
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def neighbors(loc):
   x,y = loc
   return [(x+m[0], y+m[1]) for m in moves]

dest = None

def print_map(map):
   xs = [k[0] for k in map]
   ys = [k[1] for k in map]

   t = {1:' ', 0:'#', 2:'G'}

   for y in range(max(ys), min(ys)-1, -1):
      for x in range(min(xs), max(xs)+1):
         if x == 0 and y == 0:
            print('R', end="")
         elif (x,y) in map:
            print(t[map[(x,y)]], end="")
         else:
            print("?", end="")
      print()

def dfs(map, root, robot):
   global in_dir, dest
   ms = [m for m in moves if (root[0]+m[0], root[1]+m[1]) not in map]
   for m in ms:
      loc = (root[0]+m[0], root[1]+m[1])
      # make move
      in_dir = moves.index(m)+1
      robot.run()
      result = robot.output.pop(0)
      map[loc] = result
      if result != 0:
         if result == 2:
            dest = loc
         #recurse
         dfs(map, loc, robot)
         #undo move
         in_dir = moves.index((-m[0], -m[1]))+1
         robot.run()
         robot.output.pop(0)

def scout(robot):
   global in_dir
   # 1 = valid, 0 = wall, 2 = goal
   map = {(0,0):1}
   dfs(map, (0,0), robot)
   return map

def bfs(map, start, goal):
   seen = set()
   dist = {start:0}
   q = [start]

   while len(q) > 0:
      cur = q.pop(0)
      if map[cur] == goal:
         return dist[cur]
      
      ns = [n for n in neighbors(cur) if map[n] != 0 and n not in seen]
      for n in ns:
         seen.add(n)
         dist[n] = dist[cur]+1
         q.append(n)
   # if goal not found, returns max depth of search
   return dist[cur]


with open("input.txt") as f:
   robot = IntComputer(f.read(), f_dir)

map = scout(robot)

#print_map(map)

print("Part 1:", bfs(map, (0,0), 2))
print("Part 2:", bfs(map, dest, None))
