# %%
from aocd.models import Puzzle 
puzzle = Puzzle(year = 2016, day=20)
X = [(int(y[0]), int(y[1])) for y in [x.split('-') for x in puzzle.input_data.split()]]
# %%
X.sort()
# %%
best = 0
for low, high in X:
  if best < low:
    break
  best = max(best, high+1)
best
# %%
puzzle.answer_a = best
# %%
# PART 2:
# Condense ranges to eliminate any overlap
Y = [] # new condensed IP ranges (sorted)
l, h = 0, 0

for low, high in X:
  if low > h+1:
    Y.append((l, h))
    l, h = low, high
  elif high > h:
    h = high
if (l,h) != Y[-1]:
  Y.append((l, h))

s = 0 # running sum
for i in range(1, len(Y)):
  p = Y[i-1] # prev
  c = Y[i] # current
  s += c[0] - p[1] - 1
s
# %%
puzzle.answer_b = s
