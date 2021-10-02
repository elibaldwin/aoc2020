# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=12)
# %%
X = puzzle.input_data.strip().split('\n')
#X = ['F10', 'N3', 'F7', 'R90', 'F11']
# %%
x, y = 0, 0
DIRS={'N':(0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

orientation = 0

OR_DIRS = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}

for l in X:
  d = l[0]
  n = int(l[1:])
  print(d, n)
  if d in DIRS:
    dx, dy = DIRS[d]
    x += dx * n
    y += dy * n
  elif d == 'L':
    orientation = (orientation + n) % 360
  elif d == 'R':
    orientation = (orientation - n + 360) % 360
  else:
    print("orient", orientation)
    dx, dy = OR_DIRS[orientation]
    x += dx * n
    y += dy * n
  print("pos:", x, y)

print(x,y)
    
# %%
ans = abs(x) + abs(y)
ans
# %%
puzzle.answer_a = ans
# %%
wx, wy = 10, 1
x, y = 0, 0
print("pos", x, y)
print("waypoint", wx, wy)
for l in X:
  d = l[0]
  n = int(l[1:])
  print(l)
  if d in DIRS:
    dx, dy = DIRS[d]
    wx += dx * n
    wy += dy * n
  elif d == 'L':
    rad = np.radians(n)
    R = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    P = np.array([wx, wy])
    wx, wy = R @ P
  elif d == 'R':
    rad = np.radians(-n)
    R = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    P = np.array([wx, wy])
    wx, wy = R @ P
  else:
    x += wx * n
    y += wy * n
  print("pos", x, y)
  print("waypoint", wx, wy)

ans = abs(x) + abs(y)
ans
# %%
puzzle.answer_b = int(ans)
# %%
