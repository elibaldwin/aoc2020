# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
import functools
puzzle = Puzzle(year=2020, day=24)
# %%

source = puzzle.input_data
#source = open('in24.txt', 'r').read()

X = source.strip().split('\n')
ADJ = {'nw':(0,-1), 'ne':(1, -1), 'e':(1, 0), 'se':(0, 1), 'sw':(-1, 1), 'w':(-1,0)}

def decode(dirs):
  i = 0
  q,r = 0,0
  while i < len(dirs):
    if dirs[i] in ['e', 'w']:
      d = dirs[i]
      i+=1
    else:
      d = dirs[i:i+2]
      i+=2
    dq, dr = ADJ[d]
    q+=dq
    r+=dr
  return q,r

black=set()

for line in X:
  q,r = decode(line)
  if (q,r) in black:
    black.remove((q,r))
  else:
    black.add((q,r))

print(len(black))
# %%
DIRS = list(ADJ.values())

def count_adj(tile, black):
  q,r = tile
  return sum(((q+dq, r+dr) in black) for dq,dr in DIRS)

def iter_tiles(black):
  new_black = set()

  for tile in black:
    c = count_adj(tile, black)
    if c == 1 or c == 2:
      new_black.add(tile)
  
  for q,r in black:
    for dq, dr in DIRS:
      tile = (q+dq, r+dr)
      if (tile not in black) and (tile not in new_black):
        c = count_adj(tile, black)
        if c == 2:
          new_black.add(tile)
  return new_black

for _ in range(100):
  black = iter_tiles(black)

print(len(black))

# %%
