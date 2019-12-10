def fuel_for(weight):
  total = 0
  while weight > 0:
    fuel = (weight // 3) - 2
    if (fuel > 0):
      total += fuel
    weight = fuel
  return total

with open("input.txt") as f:
  weights = [int(x) for x in f.readlines()]
  
  part1 = sum([((x // 3) - 2) for x in weights])
  print ("Part 1: ", part1)

  part2 = sum([fuel_for(x) for x in weights])
  print ("Part 2: ", part2)
