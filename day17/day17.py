from intcode import IntComputer

def f_in():
   return 0

with open("input.txt") as f:
   codestring = f.read()
   comp = IntComputer(codestring, f_in)

s = ''
comp.run()
while not comp.halted:
   s += chr(comp.output.pop(0))
   comp.run()

lines = s.strip().split('\n')

r_pos = None


rev_dir = {(0, -1): 0, (1, 0): 1, (0, 1): 2, (-1, 0): 3}
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
r_ors = ['^', '>', 'v', '<']
r_dir = 0

total = 0
for i in range(1, len(lines)-1):
   for j in range(1, len(lines[i])-1):
      if lines[i][j] == '#':
         if lines[i][j+1] == '#' and lines[i][j-1] == '#' and lines[i+1][j] == '#' and lines[i-1][j] == '#':
            total += i * j
      if lines[i][j] in r_ors:
         r_pos = (j, i)
         r_dir = r_ors.index(lines[i][j])


print("Part 1:", total)

from collections import defaultdict
map_dict = defaultdict(lambda: '.')

for i,l in enumerate(lines):
   for j, c in enumerate(l):
      map_dict[(j, i)] = c

x,y = r_pos
for m in moves:
   xx, yy = x+m[0], y+m[1]
   if map_dict[(xx,yy)] == '#':
      init_dir = rev_dir[m]

init_turn = ((init_dir - r_dir) + 4) % 4

turns = {1: ['R'], 2: ['R', 'R'], 3: ['L']}

move_list = turns[init_turn]

r_dir = (r_dir + init_turn) % 4

def gen_path(move_list, m, r, r_dir):
   global rev_dir, moves, turns
   done = False
   while not done:
      d = 0
      n = (r[0] + moves[r_dir][0], r[1] + moves[r_dir][1])
      while m[n] == '#':
         d += 1
         r = n
         n = (r[0] + moves[r_dir][0], r[1] + moves[r_dir][1])
      move_list.append(str(d))
      lt = (r_dir + 3) % 4
      rt = (r_dir + 1) % 4
      if m[(r[0] + moves[lt][0], r[1] + moves[lt][1])] == '#':
         r_dir = lt
         move_list.append('L')
      elif m[(r[0] + moves[rt][0], r[1] + moves[rt][1])] == '#':
         r_dir = rt
         move_list.append('R')
      else:
         done = True


gen_path(move_list, map_dict, r_pos, r_dir)
#print(",".join(move_list))

A = "R,6,L,10,R,8"
B = "R,8,R,12,L,8,L,8"
C = "L,10,R,6,R,6,L,8"

routine = "A,B,A,B,C,A,B,C,A,C"

def convert_s_to_ascii(A):
   A = [ord(c) for c in A]
   return A

A = convert_s_to_ascii(A)
B = convert_s_to_ascii(B)
C = convert_s_to_ascii(C)
routine = convert_s_to_ascii(routine)


in_buf = routine.copy()
in_buf.append(10)
in_buf.extend(A)
in_buf.append(10)
in_buf.extend(B)
in_buf.append(10)
in_buf.extend(C)
in_buf.append(10)


def f_inbuf():
   global in_buf
   return in_buf.pop(0)

in_buf.append(ord('n'))
in_buf.append(10)


comp2 = IntComputer("2" + codestring[1:], f_inbuf)


comp2.run()
while not comp2.halted:
   comp2.run()

print("Part 2:", comp2.output.pop())





