from intcode import IntComputer
from collections import defaultdict

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def run_turtle(code, start_color):
  global dirs
  turtle = IntComputer(code, [start_color])
  painted = defaultdict(int)
  x, y = 0, 0
  d = 0

  ys = []
  xs = []

  turtle.run()
  while not turtle.halted:
    color = turtle.output.pop(0)
    turn = turtle.output.pop(0)
    painted[(x, y)] = color
    d = (d + (1 if turn == 1 else -1)) % 4
    x += dirs[d][0]
    y += dirs[d][1]
    ys.append(y)
    xs.append(x)
    turtle.inbuf.append(painted[(x, y)])
    turtle.run()
  return (painted, xs, ys)

def print_painted(painted, xs, ys):
  for y in range(max(ys), min(ys)-1, -1):
    for x in range(min(xs), max(xs)+1):
      if painted[(x, y)] == 1:
        print('#', end="")
      else:
        print(' ', end="")
    print()
    

with open("input.txt") as f:
  code = f.read()
  painted,_,_ = run_turtle(code, 0)
  print("Part 1:", len(painted))
  painted,xs,ys = run_turtle(code, 1)
  print("Part 2:")
  print_painted(painted, xs, ys)