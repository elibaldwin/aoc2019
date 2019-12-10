with open("input.txt") as f:
  code = tuple([int(x) for x in f.read().strip().split(",")])

def run_code(code, noun, verb):
  code = list(code)

  code[1] = noun
  code[2] = verb

  pos = 0
  opcode = code[pos]

  while opcode != 99:
    in1 = code[pos+1]
    in2 = code[pos+2]
    out = code[pos+3]

    if opcode == 1:
      code[out] = code[in1] + code[in2]
    elif opcode == 2:
      code[out] = code[in1] * code[in2]
      
    pos += 4
    opcode = code[pos]
  return code[0]

def find_solution(code, goal):
  for noun in range(100):
    for verb in range(100):
      output = run_code(code, noun, verb)
      if output == goal:
        return 100 * noun + verb

print("Part 1: ", run_code(code, 12, 2))

print("Part 2: ", find_solution(code, 19690720))
