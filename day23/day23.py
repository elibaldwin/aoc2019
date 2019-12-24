from intcode import IntComputer
with open("input.txt") as f:
   code = f.read()

in_bufs = [[i] for i in range(50)]
def f_in(id):
   global in_bufs
   if in_bufs[id]:
      return in_bufs[id].pop(0)
   else:
      return -1

network = []
for i in range(50):
   network.append(IntComputer(code, f_in, i, 3))

NAT = (None, None)
last_y = 0
first = True

while any(not x.halted for x in network):
   if all(len(x) == 0 for x in in_bufs) and all(c.waiting for c in network):
      in_bufs[0].append(NAT[0])
      in_bufs[0].append(NAT[1])
      if NAT[1] == last_y:
         print("Part 2:", last_y)
         raise SystemExit()
      last_y = NAT[1]
   for i,c in enumerate(network):
      if not c.halted:
         c.run()
         if len(c.output) >= 3:
            addr = c.output.pop(0)
            X = c.output.pop(0)
            Y = c.output.pop(0)
            if addr == 255:
               if first:
                  print("Part 1:", Y)
                  first = False
               NAT = (X,Y)
               continue
            in_bufs[addr].append(X)
            in_bufs[addr].append(Y)

