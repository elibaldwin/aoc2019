from intcode import IntComputer
from collections import defaultdict
import time



pixels = defaultdict(int)
boxcount = 0

def print_screen(screen, score):
  print(f"--------------SCORE={score:5}-------------")
  for y in range(0, 21):
    for x in range(0, 38):
      print(tiles[screen[(x,y)]], end="")
    print()


tiles = {0: ' ', 1: 'X', 2: '#', 3: '_', 4: 'o'}

score = 0
inputs = {'j': -1, 'k': 0, 'l': 1}

bx = 0
px = 0
joystick = 0

def get_joystick():
  global joystick
  return joystick

with open("input2.txt") as f:
  c = IntComputer(f.read(), get_joystick, 3)

part1 = False
c.run()

while not c.halted:
  x,y = c.output.pop(0), c.output.pop(0)
  tile_id = c.output.pop(0)
  if (x == -1 and y == 0):
    score = tile_id
  else:
    pixels[(x,y)] = tile_id
    if not part1 and tile_id == 2:
      boxcount+=1
    if tile_id == 4:
      #time.sleep(0.01)
      #print_screen(pixels, score)
      bx = x
    if tile_id == 3:
      px = x
      if not part1:
        print("Part 1:", boxcount)
        part1 = True
  if bx > px:
    joystick = 1
  elif bx < px:
    joystick = -1
  else:
    joystick = 0
  c.run()

print("Part 2:", score)