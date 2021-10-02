from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2016, day=18)

in_str = puzzle.input_data
#in_str = '.^^.^.^^^^'

N_ROW = 400000

rows = np.empty((N_ROW, len(in_str)))
rows[0] = np.array([x == '^' for x in in_str])

N = len(rows[0])

def is_trap(i, arr):
  a = arr[i-1] if i > 0 else False
  b = arr[i]
  c = arr[i+1] if i < len(arr)-1 else False
  return (a and b and not c) or (not a and b and c) or (a and not b and not c) or (not a and not b and c)

for i in range(1, N_ROW):
  for j in range(N):
    rows[i,j] = is_trap(j, rows[i-1])
  if i % 1000 == 0:
    print(i)

print(rows)
print(rows.size - np.count_nonzero(rows))

puzzle.answer_b = rows.size - np.count_nonzero(rows)

