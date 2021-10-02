# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=9)
# %%
X = [int(x) for x in puzzle.input_data.strip().split('\n')]

# %%

buf = deque()
i = 0
while i < 25:
  buf.append(X[i])
  i+=1

while i < len(X):
  found = False
  for x, y in itertools.combinations(buf, 2):
    if x + y == X[i]:
      found = True
      break
  if not found:
    ans = X[i]
    print(X[i])
    break
  buf.popleft()
  buf.append(X[i])
  i+=1




# %%
puzzle.answer_a = ans
# %%
goal = ans

# %%
si = 0
ei = 2

res = []
Y = X

while si < len(Y):
  #print(si, ei)
  s = sum(Y[si:ei])
  if s == goal:
    res = Y[si:ei]
    break
  elif s < goal and ei+1 < len(X):
    ei += 1
  else:
    si += 1
    ei = si+2

  
# %%
print(min(res) + max(res))
# %%
