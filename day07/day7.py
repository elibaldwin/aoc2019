with open("day07/input.txt") as f:
  code = tuple([int(x) for x in f.read().strip().split(',')])

sysID = [0, 0]
sysID_i = 0
output = 0
numInputs = 0

def op1(code, a, b, c, pos):
  code[c] = a + b
  return pos+4

def op2(code, a, b, c, pos):
  code[c] = a * b
  return pos+4

def op3(code, a, pos):
  global sysID
  global sysID_i
  global numInputs
  code[a] = sysID[sysID_i]
  sysID_i = (sysID_i + 1)%2
  numInputs+=1
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
      break
    elif opcode == 3:
      pos = ops[2](code, code[pos+1], pos)
    else:
      if opcode != 99:
        print ("unknown opcode:", opcode)
      break


class Amp:
  def __init__(self, code, name, phase):
    self.name = name
    self.code = code
    self.pos = 0
    self.input = [phase]
    self.target = None
    self.output = None
    self.state = "run"

  def run(self):
    while True:
      opcode = self.code[self.pos] % 100
      
      a_mode = (self.code[self.pos] % 1000) // 100
      b_mode = (self.code[self.pos] % 10000) // 1000

      if opcode in [1,2,7,8]:
        a = self.code[self.code[self.pos+1]] if a_mode == 0 else self.code[self.pos+1]
        b = self.code[self.code[self.pos+2]] if b_mode == 0 else self.code[self.pos+2]
        c = self.code[self.pos+3]
        self.pos = ops[opcode-1](self.code, a, b, c, self.pos)
      elif opcode in [5, 6]:
        a = self.code[self.code[self.pos+1]] if a_mode == 0 else self.code[self.pos+1]
        b = self.code[self.code[self.pos+2]] if b_mode == 0 else self.code[self.pos+2]
        self.pos = ops[opcode-1](self.code, a, b, self.pos)
      elif opcode == 4:
        a = self.code[self.code[self.pos+1]] if a_mode == 0 else self.code[self.pos+1]
        self.target.input.append(a)
        self.output = a
        self.pos += 2
      elif opcode == 3:
        a = self.code[self.pos+1]
        if len(self.input) > 0:
          self.code[a] = self.input.pop(0)
          self.pos += 2
        else:
          return
      else:
        self.state = "halt"
        return
        
  
import itertools
outputs = []

phase_options = itertools.permutations([0,1,2,3,4])

for phases in phase_options:
  output = 0
  for phase in phases:
    sysID = [phase, output]
    run_code(list(code))
  outputs.append(output)

print("Part 1:", max(outputs))

outputs = []

phase_options = itertools.permutations([5,6,7,8,9])

names = ["A", "B", "C", "D", "E"]
for phases in phase_options:
  amps = []
  for i in range(5):
    amps.append(Amp(list(code), names[i], phases[i]))
  for i in range(5):
    amps[i].target = amps[(i+1)%5]

  amps[0].input.append(0)
  while amps[4].state != "halt":
    for amp in amps:
      if len(amp.input) > 0:
        amp.run()     
  outputs.append(amps[4].output)

print("Part 2:", max(outputs))


