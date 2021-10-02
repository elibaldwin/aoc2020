# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
puzzle = Puzzle(year=2020, day=20)
# %%
source = puzzle.input_data
#source = open('in20.txt', 'r').read()

X = source.strip().split('\n\n')

ids, tiles = [], []
h_parse = parse.compile('Tile {:d}:')

for x in X:
  lines = x.split('\n')
  id_n = h_parse.parse(lines[0])[0]
  tile = np.zeros((len(lines)-1, len(lines[1])), dtype=np.int8)
  for i, l in enumerate(lines[1:]):
    for j, c in enumerate(l):
      tile[i,j] = (c == '#')
  ids.append(id_n)
  tiles.append(tile)

# %%
def orientations(tile):
  yield tile
  for i in range(1, 4):
    yield np.rot90(tile, k=i)
  flip = np.fliplr(tile)
  yield flip
  for i in range(1, 4):
    yield np.rot90(flip, k=i)

# %%
neighbors = defaultdict(set)

def match(t1, t2):
  for a in orientations(t1):
    for side in [t2[0,:], t2[-1,:], t2[:,0], t2[:,-1]]:
      if np.array_equal(a[0,:], side):
        return True
  return False

for (t_id, tile), (o_id, other) in itertools.combinations(zip(ids, tiles), 2):
  if match(tile, other):
    neighbors[t_id].add(o_id)
    neighbors[o_id].add(t_id)

prod = 1
corners = []
for key in neighbors:
  if len(neighbors[key]) == 2:
    prod *= key
    corners.append(key)

side_length = int(np.sqrt(len(tiles)))
layout = np.zeros((side_length, side_length), dtype=np.int32)

topleft=corners[0]
layout[0,0] = topleft

layout[0,1] = neighbors[topleft].pop()
layout[1,0] = neighbors[topleft].pop()

neighbors[layout[0,1]].remove(layout[0,0])
neighbors[layout[1,0]].remove(layout[0,0])

for i in range(2, side_length):
  a, b = layout[0,i-1], layout[1,i-2]
  to_use = neighbors[a] - neighbors[b]
  neighbors[a] -= to_use
  layout[0,i] = to_use.pop()
  neighbors[layout[0,i]].remove(a)
  for j in range(1, i+1):
    to_use = neighbors[layout[j-1, i-j]].pop()
    layout[j, i-j] = to_use
    neighbors[to_use].remove(layout[j-1, i-j])
    if i-j > 0:
      neighbors[layout[j, i-j-1]].remove(to_use)
      neighbors[to_use].remove(layout[j, i-j-1])

for i in range(1, side_length):
  for j in range(0, side_length-i):
    to_use = neighbors[layout[i+j-1, -j-1]].pop()
    layout[i+j, -j-1] = to_use
    neighbors[to_use].remove(layout[i+j-1, -j-1])
    neighbors[layout[i+j, -j-2]].remove(to_use)
    neighbors[to_use].remove(layout[i+j, -j-2])

print(layout)
tilemap = {x:y for x,y in zip(ids, tiles)}

# set orientation of top-left

tl = tilemap[layout[0,0]]
a = tilemap[layout[0,1]]
b = tilemap[layout[1,0]]

for tlo in orientations(tl):
  ca = False
  for ao in orientations(a):
    if np.array_equal(tlo[:,-1], ao[:,0]):
      ca = True
      break
  cb = False
  for bo in orientations(b):
    if np.array_equal(tlo[-1,:], bo[0,:]):
      cb = True
      break
  if ca and cb:
    tilemap[layout[0,0]] = tlo
    break

for i in range(1, side_length):
  left = tilemap[layout[0,i-1]]
  cur = tilemap[layout[0,i]]
  for o in orientations(cur):
    if np.array_equal(left[:,-1], o[:,0]):
      tilemap[layout[0,i]] = o
      break

for j in range(side_length):
  for i in range(1, side_length):
    up = tilemap[layout[i-1,j]]
    cur = tilemap[layout[i,j]]
    for o in orientations(cur):
      if np.array_equal(up[-1,:], o[0,:]):
        tilemap[layout[i,j]] = o
        break

crop = tiles[0].shape[0]-2
big_sidel = side_length * crop
big_picture = np.zeros((big_sidel, big_sidel), dtype=np.int8)

for i in range(side_length):
  for j in range(side_length):
    big_picture[crop*i:crop*(i+1),crop*j:crop*(j+1)] = tilemap[layout[i,j]][1:-1,1:-1]


# %%
sm = open('seamonster.txt','r').read().split('\n')
seamonster = np.zeros((len(sm), len(sm[0])), dtype=np.int8)

for i,l in enumerate(sm):
  for j,c in enumerate(l):
    seamonster[i,j] = (c == '#')

print(seamonster)
# %%
import scipy
import scipy.ndimage
import scipy.signal
# %%
for o in orientations(big_picture):
  conv = scipy.ndimage.convolve(o, seamonster, mode='constant')
  if np.max(conv)==15:
    big_picture = o
    break

n_monsters = np.sum(conv==15)
roughness = np.sum(big_picture) - n_monsters * np.sum(seamonster)
roughness
# %%
