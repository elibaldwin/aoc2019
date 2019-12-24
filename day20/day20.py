with open("input.txt") as f:
   G = [list(x) for x in f.readlines()]

from collections import defaultdict
pps = defaultdict(list)

w = len(G[0])
h = len(G)

def neighbors(p):
   global w, h
   ns = []
   for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      x = p[0] + m[0]
      y = p[1] + m[1]
      if 0 <= x < w and 0 <= y < h:
         ns.append((x,y))
   return ns

for y, l in enumerate(G):
   for x, c in enumerate(l):
      if 'A' <= c <= 'Z':
         for nx,ny in neighbors((x,y)):
            nc = G[ny][nx]
            if 'A' <= nc <= 'Z':
               name = c + nc
               if y == 0:
                  pps[name].append((x, 2))
               elif x == 0:
                  pps[name].append((2, y))
               elif y == h - 2:
                  pps[name].append((x, h-3))
               elif x == w - 3:
                  pps[name].append((w-4, y))
               elif y < ny and y < h/2:
                  pps[name].append((x, y-1))
               elif y < ny and y > h/2:
                  pps[name].append((x, y+2))
               elif x < w/2:
                  pps[name].append((x-1, y))
               else:
                  pps[name].append((x+2, y))
               G[y][x] = ' '
               G[ny][nx] = ' '

start = pps['AA'][0]
goal = pps['ZZ'][0]

pps.pop('AA')
pps.pop('ZZ')


warps = {}
for k in pps:
   l = pps[k]
   warps[l[0]] = l[1]
   warps[l[1]] = l[0]

def nbs(G, warps, pos):
   ns = []
   for n in neighbors(pos):
      if G[n[1]][n[0]] == '.':
         ns.append(n)
   if pos in warps:
      ns.append(warps[pos])
   return ns

def nbs2(G, warps, pos, lvl):
   ns = []
   for n in neighbors(pos):
      if G[n[1]][n[0]] == '.':
         ns.append((n, lvl))
   if pos in warps and (lvl != 0 or is_inner(pos)):
      if is_inner(pos):
         ns.append((warps[pos], lvl+1))
      else:
         ns.append((warps[pos], lvl-1))
   return ns

def bfs(G, warps, start, goal):
   seen = set()
   q = [start]
   dists = {start:0}

   while q:
      cur = q.pop(0)

      if cur == goal:
         return dists[cur]
      
      for n in nbs(G, warps, cur):
         if n not in seen:
            dists[n] = dists[cur]+1
            seen.add(n)
            q.append(n)

print("Part 1:", bfs(G, warps, start, goal))

def is_inner(pos):
   global w, h
   x,y = pos
   return not (x == 2 or y == 2 or x == w-4 or y == h-3)

def bfs2(G, warps, start, goal):
   seen = set()
   q = [(start, 0)]
   dists = {(start, 0):0}
   while q:
      cur, lvl = q.pop(0)

      if cur == goal:
         if lvl == 0:
            return dists[(cur, lvl)]
         else:
            continue
      
      for n in nbs2(G, warps, cur, lvl):
         if n not in seen:
            dists[n] = dists[(cur, lvl)]+1
            seen.add(n)
            q.append(n)


print("Part 2:", bfs2(G, warps, start, goal))   





