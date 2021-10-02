# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
puzzle = Puzzle(year=2020, day=17)
# %%
X = puzzle.input_data.strip().split('\n')
#X = open('in17.txt', 'r').read().strip().split('\n')
# %%
print(X)
# %%
chart = defaultdict(bool)
r = len(X) // 2
for i, l in enumerate(X):
  for j, c in enumerate(l):
    chart[(j-r, i-r, 0, 0)]= (c == '#')
print(chart)


def count_neighbors(chart, x, y, z, w):
  c = 0
  for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
      for k in range(-1, 2, 1):
        for l in range(-1, 2, 1):
          if (not (i==0 and j==0 and k==0 and l==0)) and chart[(x+i, y+j, z+k, w+l)]:
            c+=1
  return c

def print_chart(chart, r):
  for z in range(-r, r+1):
    print('z=', z)
    for y in range(-r, r+1):
      l = ''
      for x in range(-r, r+1):
        l += '#' if chart[(x,y,z)] else '.'
      print(l)
    print()

#print_chart(chart, r)

def step(chart, r):
  nchart = defaultdict(bool)
  for x in range(-r, r+1):
    for y in range(-r, r+1):
      for z in range(-r, r+1):
        for w in range(-r, r+1):
          c = count_neighbors(chart, x,y,z,w)
          if chart[(x,y,z,w)]:
            nchart[(x,y,z,w)] = (c in [2, 3])
          else:
            nchart[(x,y,z,w)] = (c == 3)
  return nchart

for _ in range(6):
  print('iter')
  r+=1
  chart = step(chart, r)
  #print_chart(chart, r)
  

s = 0
for k in chart:
  if chart[k]:
    s+=1

s
# %%
np_chart = np.zeros((21, 21, 21, 21), dtype=np.bool)

for i, l in enumerate(X):
  for j, c in enumerate(l):
    np_chart[j+6, i+6, 0, 0] = (c == '#')

def np_count_neighbors(chart, x, y, z, w):
  return np.sum(chart[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2])-chart[x,y,z,w]

def np_step(chart):
  n_chart = np.zeros(chart.shape)
  for x in range(21):
    for y in range(21):
      for z in range(21):
        for w in range(21):
          c = np_count_neighbors(chart, x, y, z, w)
          if chart[x,y,z,w]:
            n_chart[x,y,z,w] = (c in [2,3])
          else:
            n_chart[x,y,z,w] = (c==3)
  return n_chart

#for _ in range(6):
  #np_chart = np_step(np_chart)

np.sum(np_chart)
# %%
