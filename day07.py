# %%
from aocd.models import Puzzle
import numpy as np
import itertools
from collections import Counter, defaultdict
puzzle = Puzzle(year=2020, day=7)
# %%
X = puzzle.input_data.split('\n')

can_contain = defaultdict(list)
for l in X:
  ls = l.split('contain')
  inners = ls[1].split(',')
  a = ls[0].split()
  parent = a[0] + " " + a[1]
  if 'no' in ls[1]:
    can_contain[parent] = []
    continue
  for i in inners:
    b = i.split()
    n = int(b[0])
    child = b[1] + " " + b[2]
    can_contain[parent].append((child, n))

can_contain

# %%
has_shiny = set()

def pt1(name):
  if name == 'shiny gold':
    return True
  if name in has_shiny:
    return True

  yes = False
  for v in can_contain[name]:
    if pt1(v[0]):
      yes = True
      has_shiny.add(v[0])
      has_shiny.add(name)
  return yes

s = 0
for k in can_contain.keys():
  pt1(k)

len(has_shiny)
# %%
puzzle.answer_a = s
# %%

def count_held(name):
  if can_contain[name] == []:
    return 0
  s = 0
  for v, n in can_contain[name]:
    s += n + n * count_held(v)
  return s

count_held('shiny gold')


# %%
