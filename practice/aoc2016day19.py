
# %%
from aocd.models import Puzzle
import numpy as np
import itertools
from collections import Counter
from collections import deque
puzzle = Puzzle(year=2016, day=19)
# %%
n = int(puzzle.input_data)
# %%
def josephus(n):
  bin_str = format(n, 'b')
  return int(bin_str[1:] + bin_str[0], 2)
# %%
puzzle.answer_a = josephus(n)
# %%
def part_2(n):
  ring = deque(range(1, n+1))
  r = len(ring) // 2
  ring.rotate(-r)
  step = len(ring) % 2
  while len(ring) > 1:
    ring.popleft()
    ring.rotate(-step)
    step = (step + 1) % 2
  return ring.pop()
# %%
part_2(5)
# %%
puzzle.answer_b = part_2(n)
# %%
