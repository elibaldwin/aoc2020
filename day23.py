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
puzzle = Puzzle(year=2020, day=23)
# %%

source = puzzle.input_data
#source = '389125467'



# %%

cups = deque([int(x)-1 for x in list(source)])
cups.rotate(-1)

def move(cups):
  three = [cups.popleft(), cups.popleft(), cups.popleft()]
  cur = cups[-1]
  #print(cur)
  dest = (cur-1) % len(cups)
  while dest in three:
    dest = (dest - 1) % len(cups)
  dest_i = cups.index(dest)
  cups.rotate(-(dest_i+1))
  cups.extendleft(reversed(three))
  cups.rotate(dest_i)
  #print([x+1 for x in cups])
  return cups

for _ in range(100):
  cups = move(cups)
# %%

cups = deque([int(x)-1 for x in list(source)])
for i in range(9, 1000000):
  cups.append(i)
cups.rotate(-1)

t_init = time.perf_counter()
for _ in range(20):
  print([cups[i]+1 for i in range(-8, -1)], f'({cups[-1]+1})', [cups[i]+1 for i in range(0, 10)])
  cups = move(cups)

print(time.perf_counter()-t_init)
# %%
og_cups = [int(x) for x in list(source)]
# cups[n] = number following n in the circle
cups = [0 for _ in range(1000001)]
#cups = [0 for _ in range(10)]
for i in range(len(og_cups)-1):
  cups[og_cups[i]] = og_cups[i+1]

cups[og_cups[-1]] = len(og_cups)+1
for i in range(len(og_cups)+1, 1000000):
  cups[i] = i+1
cups[1000000] = og_cups[0]

#cups[og_cups[-1]] = og_cups[0]

def printncups(cups, cur, n=15):
  s = ''
  for i in range(n-1):
    s += str(cur) + ', '
    cur = cups[cur]
  print(s + str(cur))

def move2(cups, cur):
  #print("cur", cur)
  pick1 = cups[cur]
  pick2 = cups[pick1]
  pick3 = cups[pick2]
  #print("pick up", pick1, pick2, pick3)
  dest = cur-1 if cur-1 != 0 else len(cups)-1
  while dest == pick1 or dest == pick2 or dest == pick3:
    dest = dest-1 if dest-1 != 0 else len(cups)-1
  #print("destination", dest)
  cups[cur] = cups[pick3]
  dest_next = cups[dest]
  cups[dest] = pick1
  cups[pick3] = dest_next
  return cups[cur]

# %%
cur = og_cups[0]
for i in range(10000000):
  if i % 1000000 == 999999:
    print(i)
  cur = move2(cups, cur)
print(cups[1], cups[cups[1]])
print(cups[1] * cups[cups[1]])
# %%
cur = og_cups[0]
for i in range(10):
  cur = move2(cups, cur)
  printncups(cups, cur, 9)
# %%
