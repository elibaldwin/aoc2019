with open("input.txt") as f:
   I = [x.strip().split(" ") for x in f.readlines()]

from collections import deque

length = 119315717514047
n_iter = 101741582076661

#deck = deque(range(length))

def modinv(n, p):
   return pow(n, p-2, p)

inv = {}
for i, l in enumerate(I):
   if l[1] == 'with':
      n = int(l[3])
      ninv = int(l[5])
      inv[n] = ninv

for l in I:
   if l[1] == 'with':
      l[3] = int(l[3])
      l[5] = int(l[5])
   if l[0] == 'cut':
      l[1] = int(l[1])
      
ind = 2020

offset = 0
incrmt = 1

for line in I:
   if line[0] == "deal" and line[1] == "with":
      incrmt *= modinv(line[3], length)
      incrmt %= length
   elif line[0] == "deal" and line[1] == "into":
      incrmt *= -1
      offset += incrmt
      offset %= length
   else:
      offset += incrmt * line[1]
      offset %= length

fin_incr = pow(incrmt, n_iter, length)
fin_off = offset * (1 - pow(incrmt, n_iter, length)) * modinv(1 - incrmt, length)

print((fin_off + fin_incr * 2020) % length)

'''
for i, line in enumerate(I):
   if line[0] == "deal" and line[1] == "with":
      deck = incr(deck, int(line[3]))
   elif line[0] == "deal" and line[1] == "into":
      deck.reverse()
   else:
      deck.rotate(-int(line[1]))

print(deck.index(2019))
'''