# %%
from aocd.models import Puzzle
import numpy as np
import itertools
from collections import Counter
puzzle = Puzzle(year=2020, day=6)
# %%
X = puzzle.input_data.split('\n\n')

# %%
s = 0
for l in X:
  ans = []
  ls = l.split('\n')
  for ll in ls:
    a = set()
    for c in ll:
      a.add(c)
    ans.append(a)
  b = ans[0]
  for c in ans:
    b = b.intersection(c)
  s += len(b)
# %%
puzzle.answer_a = s
# %%
s
# %%
