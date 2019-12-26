from intcode import IntComputer

in_buf = []
def f_in():
   global in_buf
   return in_buf.pop(0)

def has_in():
   return len(in_buf) > 0

def send_in(s):
   global in_buf
   for c in s:
      in_buf.append(ord(c))
   in_buf.append(10)

with open("input.txt") as f:
   c = IntComputer(f.read(), f_in, has_in)

while True:
   c.run()
   while c.output:
      print(chr(c.output.pop(0)), end="")
      c.run()
   instr = input()
   send_in(instr)
   
