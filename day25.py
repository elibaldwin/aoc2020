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
puzzle = Puzzle(year=2020, day=25)
# %%

ns = [int(x) for x in puzzle.input_data.split()]

pk1 = ns[0]
pk2 = ns[1]

def solve(base, modulo, goal):
  n = 1
  i = 0
  while n != goal:
    if i % 100000 == 0:
      print(i)
    n = (n * base) % modulo
    i += 1
  return i

exp1 = solve(7, 20201227, pk1)
exp2 = solve(7, 20201227, pk2)

enk_key = pow(pk1, exp2, 20201227)
print(enk_key, pow(pk2, exp1, 20201227))
# %%
puzzle.answer_a = enk_key
# %%
