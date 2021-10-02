# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=10)
# %%
X = [int(x) for x in puzzle.input_data.strip().split('\n')]
X.sort()
X

#X = [int(x.strip()) for x in open("in10.txt", 'r').readlines()]
#X.sort()
#X
# %%
n1diff = 1
n3diff = 1

for i in range(1, len(X)):
  diff = X[i]-X[i-1]
  if diff == 1:
    n1diff += 1
  elif diff == 3:
    n3diff += 1

print(n1diff, n3diff)
n1diff * n3diff
# %%
n_arrange = [0 for _ in range(len(X)+1)]
n_arrange[0] = 1

Y = [0] + X

for i in range(1, len(Y)):
  for j in range(1, 4):
    if i-j >= 0 and Y[i]-Y[i-j] <= 3:
      n_arrange[i] += n_arrange[i-j]

print(n_arrange[-1])
print(n_arrange)
# %%
