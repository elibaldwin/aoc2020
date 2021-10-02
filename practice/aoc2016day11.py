# %%
from aocd.models import Puzzle 
import itertools
from collections import defaultdict, deque
import numpy as np
puzzle = Puzzle(year = 2016, day=11)
# %%
print(puzzle.input_data)
floors = [['S', 'SM', 'P', 'PM'], ['T', 'R', 'RM', 'C', 'CM'], ['TM'], []]
#floors[0] += ['E', 'EM', 'D', 'DM']

# %%
def freeze(floors):
  fl = []
  for f in floors:
    fl.append(frozenset(f))
  return tuple(fl)

def freeze2(floors):
  fl = []
  for f in floors:
    n_pairs = 0
    singles = []
    for item in f:
      if len(item) == 2:
        if item[0] in f:
          n_pairs += 1
        else:
          singles.append(item)
      else:
        if item + 'M' not in f:
          singles.append(item)
    fl.append((n_pairs, tuple(singles)))
  return tuple(fl)

def is_valid(floor):
  has_gen = any(len(x) == 1 for x in floor)
  val = True
  for item in floor:
    if len(item) == 2 and item[0] not in floor and has_gen:
      val = False
  return val

def moves(f, fznfloors):
  nfs = []
  nfs.append(f+1) if f < 3 else None
  nfs.append(f-1) if f > 0 else None

  floors = [set(x) for x in fznfloors]
  moves = []
  for nf in nfs:
    for item in tuple(floors[f]):
      floors[f].remove(item)
      floors[nf].add(item)
      if is_valid(floors[f]) and is_valid(floors[nf]):
        moves.append((nf, freeze(floors)))
      floors[nf].remove(item)
      floors[f].add(item)
      
    for i1, i2 in itertools.combinations(floors[f], 2):
      l1, l2 = len(i1), len(i2)
      t1, t2 = i1[0], i2[0]
      if l1 != l2 and t1 != t2:
        continue # incompatible parts for same elevator
      floors[f].remove(i1)
      floors[f].remove(i2)
      floors[nf].add(i1)
      floors[nf].add(i2)
      if is_valid(floors[f]) and is_valid(floors[nf]):
        moves.append((nf, freeze(floors)))
      floors[nf].remove(i1)
      floors[nf].remove(i2)
      floors[f].add(i1)
      floors[f].add(i2)
  return moves

def bfs(floors):
  f = freeze(floors)
  f2 = freeze2(floors)

  Q = deque()
  Q.append((0, f))

  seen = set()
  seen.add((0, f2))

  dist = {(0, f):0}
  step = 0

  while Q:
    # elevator pos, floors
    cur = Q.popleft()
    e, fs = cur

    if dist[cur] > step:
      print(step)
      step = dist[cur]

    if len(fs[3]) == 14: # done!
      return dist[cur]
    
    for m in moves(e, fs):
      f2 = (m[0], freeze2(m[1]))
      if f2 not in seen:
        seen.add(f2)
        Q.append(m)
        dist[m] = dist[cur]+1
  
  return "fail"

print(bfs(floors))
#print(freeze2(floors))


# %%
