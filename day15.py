# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=15)
# %%
X = [int(x) for x in puzzle.input_data.strip().split(',')]
#X = [int(x) for x in open('in15.txt', 'r').read().strip().split(',')]
X
# %%

turn = dict()
i = 0
while i < len(X)-1:
  turn[X[i]] = i
  i += 1

i+=1
prev = X[-1]

while i < 30000000:
  if prev in turn:
    n = i - turn[prev] - 1
  else:
    n = 0
  turn[prev] = i - 1
  prev = n
  i += 1

prev
# %%

# %%
puzzle.answer_a =