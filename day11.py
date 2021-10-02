# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=11)
# %%
X = [list(x) for x in puzzle.input_data.strip().split('\n')]
#X = [list(x.strip()) for x in open('in11t.txt', 'r').readlines()]
M = X
M
# %%

def step(M):
  N = [x.copy() for x in M]
  changed = False
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == '.':
        continue
      n_occ = 0
      for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
          if k == 0 and l == 0:
            continue
          x = i + k
          y = j + l
          if 0 <= x < len(M) and 0 <= y < len(M[0]):
            if M[x][y] == '#':
              n_occ+=1
      if M[i][j] == 'L' and n_occ == 0:
        N[i][j] = '#'
        changed = True
      elif M[i][j] == '#' and n_occ >= 4:
        N[i][j] = 'L'
        changed = True
  return changed, N
      
changed = True
while(changed):
  changed, M = step(M)
  #print(np.array(M))

N = np.array(M)
res = (N[N == '#']).size
print(res)
N


# %%
N.shape
# %%

X = np.array([list(x) for x in puzzle.input_data.strip().split('\n')])
#X = np.array([list(x.strip()) for x in open('in11t.txt', 'r').readlines()])
Y = np.zeros(X.shape, X.dtype)

DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1)]

def update(X, prev, counts, i, j):
  if prev == '#' and X[i,j] != '.':
    counts[i,j]+=1
  if X[i,j] != '.':
    prev = X[i,j]
  return prev

def step(X, Y):
  counts = np.zeros(X.shape)
  # rows
  for i in range(X.shape[0]):
    prev = 'L'
    for j in range(X.shape[1]):
      prev = update(X, prev, counts, i, j)
    prev = 'L'
    for j in range(X.shape[1]-1, -1, -1):
      prev = update(X, prev, counts, i, j)
  # cols
  for i in range(X.shape[1]):
    prev = 'L'
    for j in range(X.shape[0]):
      prev = update(X, prev, counts, j, i)
    prev = 'L'
    for j in range(X.shape[0]-1, -1, -1):
      prev = update(X, prev, counts, j, i)
  # diags
  for i in range(X.shape[0]):
    prev = 'L'
    for j in range(X.shape[1]):
      if (i+j) % X.shape[0] == 0:
        prev = 'L'
      prev = update(X, prev, counts, (i+j) % X.shape[0], j)
    prev = 'L'
    for j in range(X.shape[1]):
      if (i-j) % X.shape[0] == X.shape[0]-1:
        prev = 'L'
      prev = update(X, prev, counts, (i-j) % X.shape[0], j)
  for i in range(X.shape[0]):
    prev = 'L'
    for j in range(X.shape[1]):
      if (i+j) % X.shape[0] == 0:
        prev = 'L'
      prev = update(X, prev, counts, (i+j) % X.shape[0], X.shape[1]-j-1)
    prev = 'L'
    for j in range(X.shape[1]):
      if (i-j) % X.shape[0] == X.shape[0]-1:
        prev = 'L'
      prev = update(X, prev, counts, (i-j) % X.shape[0], X.shape[1]-j-1)
  
  np.copyto(Y, X)
  cond1 = (X == 'L') & (counts == 0)
  Y[cond1] = '#'
  cond2 = (X == '#') & (counts >= 5)
  Y[cond2] = 'L'
  return np.any(cond1) or np.any(cond2)
  


# %%
cont = True
while cont:
  cont = step(X, Y)
  #print(Y)
  print(Y[(Y == '#')].size)
  if cont:
    cont = step(Y, X)
    #print(X)
    print(X[(X == '#')].size)


# %%
