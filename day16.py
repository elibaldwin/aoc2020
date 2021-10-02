# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
puzzle = Puzzle(year=2020, day=16)
# %%
p = parse.compile("{}: {:d}-{:d} or {:d}-{:d}")

X = [x.split('\n') for x in puzzle.input_data.strip().split('\n\n')]
categories = []
for l in X[0]:
  r = p.parse(l)
  categories.append((r[0], (r[1], r[2]), (r[3], r[4])))
my_ticket = [int(x) for x in X[1][1].split(',')]
tickets = [[int(x) for x in l.split(',')] for l in X[2][1:]]
cat_names = [c[0] for c in categories]
# %%
def is_valid(n, categories):
  for c in categories:
    for lb, ub in c[1:]:
      if lb <= n <= ub:
        return True
  return False

valid_tickets = []
for t in tickets:
  val = True
  for n in t:
    if not is_valid(n, categories):
      val = False
      break
  if val:
    valid_tickets.append(t)

# %%
def valid_cats(n):
  res = set()
  for c in categories:
    for lb, ub in c[1:]:
      if lb <= n <= ub:
        res.add(c[0])
  return res

ind_cats = dict()

for j in range(len(valid_tickets[0])):
  cats = valid_cats(valid_tickets[0][j])
  for i in range(1, len(valid_tickets)):
    cats = cats.intersection(valid_cats(valid_tickets[i][j]))
  ind_cats[j] = cats

cat_ind = dict()

done = False
while not done:
  found = False
  for i in list(ind_cats.keys()):
    if len(ind_cats[i]) == 1:
      found = True
      name = list(ind_cats[i])[0]
      print(name)
      cat_ind[name] = i
      del ind_cats[i]
      for s in ind_cats.values():
        s.remove(name)
      break
  done = not found

print(cat_ind)
# %%
p = 1
for cat in cat_ind:
  if "departure" in cat:
    p *= my_ticket[cat_ind[cat]]
p
# %%
puzzle.answer_b = p
# %%
