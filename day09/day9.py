from intcode import IntComputer

with open("day09/input.txt") as f:
  s = f.read()
  c = IntComputer(s, [1])
  c.run()
  print("Part 1:", c.output[0])
  c = IntComputer(s, [2])
  c.run()
  print("Part 2:", c.output[0])