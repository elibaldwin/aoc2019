
from collections import defaultdict

class IntComputer:

  # OpCode 1 is addition; adds the values at args[0] and args[1] and stores
  # them at args[2]
  def op1(self, args):
    self.code[args[2]] = self.code[args[0]] + self.code[args[1]]
    self.pos += 4

  # OpCode 2 is multiplication; multiplies the values at args[0] and args[1]
  # and stores them at args[2]
  def op2(self, args):
    self.code[args[2]] = self.code[args[0]] * self.code[args[1]]
    self.pos += 4

  # OpCode 3 is input; takes input from the input buffer and stores it at args[0]
  def op3(self, args):
    self.code[args[0]] = self.f_in()
    self.pos += 2

  # OpCode 4 is output; puts value from args[0] into output buffer
  def op4(self, args):
    self.output.append(self.code[args[0]])
    self.pos += 2

  # OpCode 5 is jump-if-true; sets pos to code[args[1]] if code[args[0]] != 0
  def op5(self, args):
    self.pos = self.code[args[1]] if self.code[args[0]] != 0 else self.pos + 3

  # OpCode 6 is jump-if-false; sets pos to code[args[1]] if code[args[0]] == 0
  def op6(self, args):
    self.pos = self.code[args[1]] if self.code[args[0]] == 0 else self.pos + 3

  # OpCode 7 is less-than; store the result of (code[args[0]] < code[args[1]]), either 1
  # or 0, to the location args[2]
  def op7(self, args):
    self.code[args[2]] = 1 if self.code[args[0]] < self.code[args[1]] else 0
    self.pos += 4

  # OpCode 8 is equals; store the result of (code[args[0]] == code[args[1]]), either 1 or 0,
  # to the location args[2]
  def op8(self, args):
    self.code[args[2]] = 1 if self.code[args[0]] == self.code[args[1]] else 0
    self.pos += 4

  # OpCode 9 adjusts the value of rbase by the value stored at args[0]
  def op9(self, args):
    self.rbase += self.code[args[0]]
    self.pos += 2

  def __init__(self, codestring, f_in, has_in, outbuflen=1):
    # input fuction
    self.f_in = f_in
    # output buffer
    self.output = []
    # number of outputs to store before returning
    self.outbuflen = outbuflen
    # defaultdict(int) stores instructions and allows for "boundless" memory
    self.code = defaultdict(int)
    # initialize with the values from the input codestring (comma-delimited)
    for i,x in enumerate(codestring.strip().split(',')):
      self.code[i] = int(x)

    self.init_c = self.code.copy()
    # stores the base location for relative position parameters
    self.rbase = 0
    # stores the current instruction pointer position
    self.pos = 0
    # list of possible operations
    self.ops = [self.op1, self.op2, self.op3, self.op4, self.op5, 
                self.op6, self.op7, self.op8, self.op9]
    self.halted = False
    self.waiting = False
    self.has_in = has_in
  
  def reset(self):
    self.code = self.init_c.copy()
    self.pos = 0
    self.rbase = 0
    self.halted = False
    self.waiting = False
    self.output = []
  
  def run(self):
    mods = [100, 1000, 10000, 100000]
    while True:
      opcode = self.code[self.pos] % 100
      args = []
      for i in [0,1,2]:
        mode = (self.code[self.pos] % mods[i+1]) // mods[i]
        if mode == 0:
          args.append(self.code[self.pos+i+1])
        elif mode == 1:
          args.append(self.pos+1+i)
        else:
          args.append(self.code[self.pos+i+1]+self.rbase)
      
      if opcode == 4:
        self.ops[3](args)
        if (len(self.output)) == self.outbuflen:
          return
      elif opcode == 3 and not self.has_in():
        return
      elif 1 <= opcode <= 9:
        self.ops[opcode-1](args)
      else:
        if opcode != 99:
          print ("unknown opcode:", opcode)
        self.halted = True
        return
  