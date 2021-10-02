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
puzzle = Puzzle(year=2020, day=21)
# %%
source = puzzle.input_data.strip()
#source = open('in21.txt', 'r').read().strip()

X = [(set(a.split()), set(b.split(', '))) for a,b in \
     [parse.parse('{} (contains {})', x) for x in source.split('\n')]]
# %%

allergens = functools.reduce(lambda a,b: a|b, (b for _,b in X), set())
ingredients = functools.reduce(lambda a,b: a|b, (a for a,_ in X), set())

all_ings = dict()

for a in allergens:
  possible = ingredients.copy()
  for ings, alls in X:
    if a in alls:
      possible &= ings
  all_ings[a] = possible

notdone = True
ing_alls = dict()
while notdone:
  notdone = False
  for a in allergens:
    if len(all_ings[a])==1:
      notdone=True
      ing = all_ings[a].pop()
      ing_alls[ing] = a
      for b in allergens:
        if ing in all_ings[b]:
          all_ings[b].remove(ing)

s = 0
for ings, alls in X:
  for i in ings:
    if i not in ing_alls:
      s+=1
print("part 1: ", s)
dangerous = [(ing_alls[a], a) for a in ing_alls.keys()]
dangerous.sort()
print("part 2: ", ','.join([b for a, b in dangerous]))
# %%
