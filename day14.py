# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=14)
# %%
X = puzzle.input_data.strip().split('\n')
#X = open('in14.txt', 'r').read().strip().split('\n')

X = [x.split() for x in X]
# %%
mem = dict()
mask = ''

def applymask(n, mask):
  n |= int(mask.replace('X', '0'), 2)
  n &= int(mask.replace('X', '1'), 2)
  return n

for l in X:
  if l[0] == 'mask':
    mask = l[2]
  else:
    i = int(l[0].split('[')[1][:-1])
    n = int(l[2])
    mem[i] = applymask(n, mask)
  

s = sum(mem.values())
s

# %%
def genmasks(mask):
  if not mask:
    yield ''
    return
  else:
    for m in genmasks(mask[1:]):
      c = mask[0]
      if c == '0':
        yield 'X' + m
      elif c == '1':
        yield '1' + m
      else:
        yield '0' + m
        yield '1' + m

mem = dict()
for l in X:
  if l[0] == 'mask':
    mask = l[2]
  else:
    i = int(l[0].split('[')[1][:-1])
    n = int(l[2])
    for m in genmasks(mask):
      mem[applymask(i, m)] = n

print(len(mem))
print(sum(mem.values()))

puzzle.answer_b = sum(mem.values())

# %%

# assumes m1 and m2 have same length
# returns mask representing addresses in m1 not blocked by m2


# %%
