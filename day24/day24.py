with open("input.txt") as f:
   G = [list(x.strip()) for x in f.readlines()]

def bio_sum(G):
   s = 0
   n = 1
   for l in G:
      for c in l:
         s += n if c == '#' else 0
         n *= 2
   return s


DR = [0, 0, 1, -1]
DC = [1, -1, 0, 0]
def count_ns(G, r, c):
   global DR, DC
   s = 0
   for i in range(4):
      if (0 <= (DR[i]+r) < 5) and (0 <= (DC[i]+c) < 5):
         s += 1 if G[r+DR[i]][c+DC[i]] == '#' else 0
   return s 


def inc(G, D):
   for r in range(5):
      for c in range(5):
         count = count_ns(G, r, c)
         cur = G[r][c] == '#'
         if cur:
            D[r][c] = '#' if count == 1 else '.'
         else:
            D[r][c] = '#' if count in [1,2] else '.'

def print_g(G):
   for r in G:
      print(''.join(r))

def get_empty_lvl():
   return [['.' for _ in range(5)] for _ in range(5)]

from copy import deepcopy

A = deepcopy(G)
B = [['.' for _ in range(5)] for _ in range(5)]

seen = set([bio_sum(A)])
while(True):
   inc(A, B)
   s = bio_sum(B)
   if s in seen:
      print("Part 1:", s)
      break
   seen.add(s)
   inc(B,A)
   s = bio_sum(A)
   if s in seen:
      print("Part 1:", s)
      break
   seen.add(s)

from collections import defaultdict

# format: [G, [sidecounts]]
lvls = defaultdict(lambda: [get_empty_lvl(), [0 for _ in range(4)]])


def update_sidecounts(lvl):
   G, counts = lvl
   counts[0] = 0
   for i in range(5):
      counts[0] += 1 if G[0][i] == '#' else 0
   counts[1] = 0
   for i in range(5):
      counts[1] += 1 if G[i][4] == '#' else 0
   counts[2] = 0
   for i in range(5):
      counts[2] += 1 if G[4][i] == '#' else 0
   counts[3] = 0
   for i in range(5):
      counts[3] += 1 if G[i][0] == '#' else 0

def count_ns2(lvls, lvl, r, c):
   s = 0
   for i, m in enumerate([(1, 0), (0, -1), (-1, 0), (0, 1)]):
      nr = r + m[0]
      nc = c + m[1]
      if nr == 2 and nc == 2:
         s += lvls[lvl+1][1][i]
      elif nr == -1:
         s += 1 if lvls[lvl-1][0][1][2] == '#' else 0
      elif nr == 5:
         s += 1 if lvls[lvl-1][0][3][2] == '#' else 0
      elif nc == -1:
         s += 1 if lvls[lvl-1][0][2][1] == '#' else 0
      elif nc == 5:
         s += 1 if lvls[lvl-1][0][2][3] == '#' else 0
      else:
         s += 1 if lvls[lvl][0][nr][nc] == '#' else 0
   return s

def inc2(lvls, lvl, limit):
   B = get_empty_lvl()
   A = lvls[lvl]
   for r in range(5):
      for c in range(5):
         if r == 2 and c == 2:
            continue
         cur = A[0][r][c] == '#'
         count = count_ns2(lvls, lvl, r, c)
         if cur:
            B[r][c] = '#' if count == 1 else '.'
         else:
            B[r][c] = '#' if count in [1,2] else '.'
   if abs(lvl) < limit and lvl <= 0:
      inc2(lvls, lvl-1, limit)
   if abs(lvl) < limit and lvl >= 0:
      inc2(lvls, lvl+1, limit)
   A[0] = B
   update_sidecounts(A)

def sum_bugs(lvls):
   s = 0
   for k in lvls:
      G = lvls[k][0]
      for r in range(5):
         for c in range(5):
            if G[r][c] == '#':
               s+=1
   return s

lvl0 = [G, [0 for _ in range(4)]]
update_sidecounts(lvl0)

lvls[0] = lvl0

for i in range(200):
   inc2(lvls, 0, i+1)

print("Part 2:", sum_bugs(lvls))



