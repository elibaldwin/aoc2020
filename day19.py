# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
puzzle = Puzzle(year=2020, day=19)
# %%
rules, messages = [x.strip().split('\n') for x in puzzle.input_data.split('\n\n')]
rules, messages = [x.split('\n') for x in open('in19.txt', 'r').read().strip().split('\n\n')]

M = dict()

for line in rules:
  l, r = line.split(': ')
  if '\"' in r:
    M[int(l)] = r.replace('\"', '')
  else:
    r = [x.split() for x in r.split(' | ')]
    M[int(l)] = tuple(tuple(int(y) for y in x) for x in r)


def count_combinations(key):
  if type(M[key]) == str:
    return 1
  else:
    s = 0
    for x in M[key]:
      s += np.prod([count_combinations(a) for a in x])
    return s

W = defaultdict(set)

def gen_words(key):
  if key in W:
    return W[key]
  else:
    r = M[key]
    if type(r) == str:
      W[key] = {r}
      return W[key]
    else:
      s = set()
      for a in r:
        s.update(''.join(x) for x in itertools.product(*(gen_words(b) for b in a)))
      W[key] = s
      return s
# %%

R = dict()

def get_regex(key):
  if key in R:
    return R[key]
  else:
    rhs = M[key]
    if key == 8:
      return get_regex(42) + '+'
    elif key == 11:
      left = get_regex(42)
      right = get_regex(31)
      res = '(?:' + '|'.join(f'{left}{{{n}}}{right}{{{n}}}' for n in range(20)) + ')'
      R[key] = res
      return res

    if type(rhs) == str:
      R[key] = rhs
      return rhs
    else:
      regexes = []
      for opt in rhs:
        regexes.append(''.join(get_regex(x) for x in opt))
      res = '(?:' + '|'.join(regexes) + ')'
      R[key] = res
      return res

# %%
import re
p = re.compile(get_regex(0))
s = 0
for m in messages:
  if p.fullmatch(m):
    print(m)
    s+=1

s
# %%
