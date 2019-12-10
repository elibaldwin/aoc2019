with open("input.txt") as f:
  code = tuple([int(x) for x in f.read().strip().split(',')])

sysID = 1
output = None

def op1(code, a, b, c, pos):
  code[c] = a + b
  return pos+4

def op2(code, a, b, c, pos):
  code[c] = a * b
  return pos+4

def op3(code, a, pos):
  global sysID
  code[a] = sysID
  return pos+2

def op4(code, a, pos):
  global output
  output = a
  return pos+2

def op5(code, a, b, pos):
  return b if a != 0 else pos+3

def op6(code, a, b, pos):
  return b if a == 0 else pos+3

def op7(code, a, b, c, pos):
  code[c] = 1 if a < b else 0
  return pos+4

def op8(code, a, b, c, pos):
  code[c] = 1 if a == b else 0
  return pos+4

ops = [op1, op2, op3, op4, op5, op6, op7, op8]

def run_code(code):
  pos = 0
  while True:
    opcode = code[pos] % 100
    
    a_mode = (code[pos] % 1000) // 100
    b_mode = (code[pos] % 10000) // 1000

    if opcode in [1,2,7,8]:
      a = code[code[pos+1]] if a_mode == 0 else code[pos+1]
      b = code[code[pos+2]] if b_mode == 0 else code[pos+2]
      c = code[pos+3]
      pos = ops[opcode-1](code, a, b, c, pos)
    elif opcode in [5, 6]:
      a = code[code[pos+1]] if a_mode == 0 else code[pos+1]
      b = code[code[pos+2]] if b_mode == 0 else code[pos+2]
      pos = ops[opcode-1](code, a, b, pos)
    elif opcode == 4:
      a = code[code[pos+1]] if a_mode == 0 else code[pos+1]
      pos = ops[3](code, a, pos)
    elif opcode == 3:
      pos = ops[2](code, code[pos+1], pos)
    else:
      if opcode != 99:
        print ("unknown opcode:", opcode)
      break


run_code(list(code))
print("Part 1:", output)
sysID = 5
run_code(list(code))
print("Part 2:", output)  

