# %%
from aocd.models import Puzzle 
import itertools
import numpy as np
puzzle = Puzzle(year = 2016, day=22)
rows, cols = 33, 29

#%%
data = [x.split() for x in puzzle.input_data.split('\n')[2:]]
nodes = [[None for _ in range(cols)] for _ in range(rows)]
ns = []
for l in data:
  n = [int(x[1:]) for x in l[0].split('-')[1:]]
  sua = tuple([int(x[:-1]) for x in l[1:-1]])
  nodes[n[0]][n[1]] = sua
  ns.append(tuple(n))

# %%
def viable(a, b, nodes):
  na = nodes[a[0]][a[1]]
  nb = nodes[b[0]][b[1]]
  return na[1] != 0 and na[1] <= nb[2]

n_viable = 0
for n1, n2 in itertools.combinations(ns, 2):
  n_viable += 1 if viable(n1, n2, nodes) else 0
  n_viable += 1 if viable(n2, n1, nodes) else 0

n_viable

# %%
puzzle.answer_a = n_viable
# %%
np_ns = np.array(nodes)
# %%
np.min(np_ns[:, :, 1])
# %%
for x in range(rows):
  line = ''
  for y in range(cols):
    c = '. '
    if x == 0 and y == 0:
      c = 'O '
    elif np_ns[x, y, 1] == 0:
      c = '_ '
    elif np_ns[x, y, 1] > 400:
      c = '# '
    elif x == rows-1 and y == 0:
      c = 'G '
    line += c
  print(line)
# Now, stare at the console and figure it out by hand :)
# %%
