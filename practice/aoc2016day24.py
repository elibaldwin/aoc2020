# %%
from aocd.models import Puzzle 
import itertools
from collections import defaultdict, deque
import numpy as np
puzzle = Puzzle(year = 2016, day=24)
# %%
plan = []
locs = dict()
locs_rev = dict()
for i, l in enumerate(puzzle.input_data.split('\n')):
  plan_line = []
  for j, c in enumerate(l):
    if c.isnumeric():
      locs[int(c)] = (i,j)
      locs_rev[(i,j)] = int(c)
      plan_line.append(True)
    elif c == '#':
      plan_line.append(False)
    else:
      plan_line.append(True)
  plan.append(plan_line)
plan = np.array(plan)

# %%
graph = dict()

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs_plan(start, plan, graph):
  Q = deque()
  Q.append(start)

  dist = dict()
  dist[start] = 0

  seen = set()
  seen.add(start)

  while Q:
    x, y = Q.popleft()

    if (x,y) != start and (x,y) in locs_rev:
      l1 = locs_rev[start]
      l2 = locs_rev[(x,y)]
      graph[(l1, l2)] = dist[(x,y)]
    
    for dx, dy in DIRS:
      if plan[x+dx,y+dy]:
        n = (x+dx, y+dy)
        if n not in seen:
          seen.add(n)
          dist[n] = dist[(x,y)]+1
          Q.append(n)

for l in locs_rev.keys():
  bfs_plan(l, plan, graph)

graph

# %%
def try_paths(startloc, graph, return_to_start):
  global locs
  loc_list = list(locs.keys())
  loc_list.remove(startloc)

  best = 9999999999
  for order in itertools.permutations(loc_list):
    prev = startloc
    d = 0
    for loc in order:
      d += graph[(prev, loc)]
      prev = loc
    if return_to_start:
      d += graph[(prev, startloc)]
    if d < best:
      print(d)
    best = min(best, d)
  return best

puzzle.answer_a = try_paths(0, graph, False)
puzzle.answer_b = try_paths(0, graph, True)

# %%
