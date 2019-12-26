from intcode import IntComputer

with open("1.ss") as f:
   sscrpt = f.read()

in_buf = [ord(c) for c in list(sscrpt)]
def f_in():
   global in_buf
   return in_buf.pop(0)

with open("input.txt") as f:
   c = IntComputer(f.read(), f_in)

c.run()

while not c.halted:
   out = c.output.pop(0)
   if out > 128:
      print("Part 1:", out)
      break
   #print(chr(out), end="")
   c.run()

with open("2.ss") as f:
   sscrpt = f.read()

in_buf = [ord(c) for c in list(sscrpt)]

with open("input.txt") as f:
   c = IntComputer(f.read(), f_in)

c.run()

while not c.halted:
   out = c.output.pop(0)
   if out > 128:
      print("Part 2:", out)
      break
   #print(chr(out), end="")
   c.run()
