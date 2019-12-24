from collections import defaultdict, namedtuple
from queue import PriorityQueue

with open("input.txt") as f:
   lines = [x.strip() for x in f.readlines()]

M = {}
s = None

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n_keys = 0
door_ps = {}
keys_ps = {}

for y, l in enumerate(lines):
   for x, c in enumerate(l):
      M[(x,y)] = c
      if c in lowers:
         n_keys += 1
         keys_ps[c] = (x,y)
      if c in uppers:
         door_ps[c] = (x,y)
      if c == '@':
         s = (x,y)
         M[(x,y)] = '.'

def neighbors(M, pos):
   ns = []
   for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      n = (pos[0] + m[0], pos[1]+ m[1])
      if n in M and M[n] != '#':
         ns.append(n)
   return ns

def bfs(M, s, dbtws):
   global lowers, uppers
   seen = set()
   dists = {s:0}
   q = [s]
   keys = []
   doors = []

   while len(q) > 0:
      cur = q.pop(0)

      for n in neighbors(M, cur):
         if n not in seen:
            c = M[n]
            if c in uppers:
               doors.append((c, n))
               seen.add(n)
               q.append(n)
            else:
               if c in lowers:
                  dbtws[(s, n)] = dists[cur]+1
                  dbtws[(n, s)] = dists[cur]+1
                  keys.append((c, n))
               seen.add(n)
               q.append(n)
            dists[n] = dists[cur] + 1
   
   return (keys, dists)

blocked = defaultdict(list)
def find_blocked(M, s):
   global lowers, uppers
   seen = set()
   q = [s]
   doors_before = defaultdict(list)
   blocked = defaultdict(set)

   while len(q) > 0:
      cur = q.pop()

      for n in neighbors(M, cur):
         if n not in seen:
            c = M[n]
            if c in uppers:
               ds = []
               ds.extend(doors_before[cur])
               ds.append(c)
               doors_before[n] = ds
            else:
               ds = doors_before[cur]
               if c in lowers:
                  for door in ds:
                     blocked[door].add(c)
               doors_before[n] = ds
            seen.add(n)
            q.append(n)
   return blocked

all_keys = set(keys_ps.keys())

def djikstra(dist_map, s, blocked):
   global n_keys, all_keys, keys_ps
   q = PriorityQueue()
   # (dist, pos, keys)
   q.put((0, s, set()))
   count = 0
   seen = set()

   while q:
      dist, pos, keys = q.get()

      uniq = (pos, frozenset(keys))
      if uniq in seen:
         continue
      seen.add(uniq)

      if len(keys) == n_keys:
         return dist
      
      options = all_keys - keys
      for k in (all_keys - keys):
         options -= blocked[k.upper()]
      
      for opt in options:
         newdist = dist + dist_map[(pos, keys_ps[opt])]
         newkeys = set(keys)
         newkeys.add(opt)
         q.put((newdist, keys_ps[opt], newkeys))
      count+=1


blocked = find_blocked(M, s)

dist_map = {}
bfs(M, s, dist_map)
for c in keys_ps:
   bfs(M, keys_ps[c], dist_map)

print("Part 1:", djikstra(dist_map, s, blocked))

with open("input2.txt") as f:
   lines = [x.strip() for x in f.readlines()]

M = {}
s = None

rs = []
n_keys = 0
keys_ps = {}
door_ps = {}
for y, l in enumerate(lines):
   for x, c in enumerate(l):
      M[(x,y)] = c
      if c in lowers:
         n_keys += 1
         keys_ps[c] = (x,y)
      if c in uppers:
         door_ps[c] = (x,y)
      if c == '@':
         rs.append((x,y))
         M[(x,y)] = '.'

dist_map = {}
for r in rs:
   bfs(M, r, dist_map)
for c in keys_ps:
   bfs(M, keys_ps[c], dist_map)

def djikstra2(dist_map, rs, blocked):
   global n_keys, all_keys, keys_ps
   q = PriorityQueue()
   # (dist, pos_list, keys)
   q.put((0, tuple(rs), set()))
   count = 0
   seen = set()

   while q:
      dist, pos_list, keys = q.get()

      uniq = (tuple(pos_list), frozenset(keys))
      if uniq in seen:
         continue
      seen.add(uniq)

      if len(keys) == n_keys:
         return dist
      
      options = all_keys - keys
      for k in (all_keys - keys):
         options -= blocked[k.upper()]

      for i, r in enumerate(pos_list):
         for opt in options:
            if (r, keys_ps[opt]) in dist_map:
               newdist = dist + dist_map[(r, keys_ps[opt])]
               newkeys = set(keys)
               newkeys.add(opt)
               newplist = list(pos_list)
               newplist[i] = keys_ps[opt]
               q.put((newdist, tuple(newplist), newkeys))
      count+=1

print("Part 2:", djikstra2(dist_map, rs, blocked))