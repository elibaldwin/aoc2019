pattern = [0, 1, 0, -1]

with open("input.txt") as f:
   s = f.read().strip()
   ind = int(s[:7])
   A = [int(x) for x in s]


def get_pattern(n):
   base = [0, 1, 0, -1]
   if n == 1:
      return base
   else:
      return [0] * n + [1] * n + [0] * n + [-1] * n

def get_p_digit(i, n):
   global pattern
   return pattern[((i+1) // n) % 4]

def inc(A, out):
   for i in range(len(A)):
      ind = [A[j] * get_p_digit(j, i+1) for j in range(i,len(A))]
      out[i] = abs(sum(ind)) % 10

def inc2(A, out):
   s = 0
   for i in range(len(A)-1, -1, -1):
      s += A[i]
      out[i] = abs(s) % 10


B = [0] * len(A)
for i in range(50):
   inc(A, B)
   inc(B, A)

A = ''.join([str(i) for i in A])
print("Part 1:", A[:8])

A = [int(c) for c in s]
A = A * 10000

A = A[ind:]
B = [0] * len(A)
for i in range(50):
   inc2(A, B)
   inc2(B, A)

print("Part 2:", ''.join([str(x) for x in A[:8]]))


