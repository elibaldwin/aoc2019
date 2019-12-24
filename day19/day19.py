from intcode import IntComputer


in_buf = []
def f_in():
   global in_buf
   return in_buf.pop(0)


with open("input.txt") as f:
   text = f.read()
   
def scan():
   global text, in_buf
   s = 0
   c = IntComputer(text, f_in)
   rep = {0:'.', 1:'#'}
   f_edges = []
   r_edges = []
   points = {}
   for x in range(1074, 1179):
      in_beam = False
      for y in range(1724, 1830):
         in_buf.append(x)
         in_buf.append(y)
         c.run()
         if c.output:
            o = c.output.pop()
            s += o
            if o == 1 and not in_beam:
               f_edges.append((x,y))
               in_beam = True
            if in_beam and o == 0:
               r_edges.append((x, y-1))
               in_beam = False
            points[(x,y)] = o
            print(rep[o], end="")
         c.reset()
      print()

   import math
   f_thetas = []
   f_edges.pop(0)
   r_edges.pop(0)
   for p in f_edges:
      f_thetas.append(math.degrees(math.atan(p[0]/p[1])))

   r_thetas = []
   for p in r_edges:
      r_thetas.append(math.degrees(math.atan(p[0]/p[1])))

   print(f_thetas)
   print(r_thetas)

   f_avg = sum(f_thetas)/len(f_thetas)
   r_avg = sum(r_thetas)/len(r_thetas)


   print(f_avg)
   print(r_avg)
   print("min/max f", min(f_thetas), max(f_thetas))
   print("min/max r", min(r_thetas), max(r_thetas))

def check(x,y):
   global text, in_buf
   outs = []
   c = IntComputer(text, f_in)
   in_buf.append(x)
   in_buf.append(y)
   c.run()
   outs.append(c.output.pop())
   c.reset()
   in_buf.append(x+99)
   in_buf.append(y)
   c.run()
   outs.append(c.output.pop())
   c.reset()
   in_buf.append(x)
   in_buf.append(y+99)
   c.run()
   outs.append(c.output.pop())
   return all(o == 1 for o in outs)

print(check(1078, 1730))
print(check(1077, 1728))
print(check(1075, 1725))


for x in range(1040, 1080):
   for y in range(1660, 1750):
      if check(x,y):
         print((x,y))

