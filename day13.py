# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
puzzle = Puzzle(year=2020, day=13)
# %%
X = puzzle.input_data.strip().split('\n')
#X = open('in13.txt', 'r').readlines()

# %%

start = int(X[0])
ids = [int(x) for x in X[1].split(',') if x != 'x']
ids
# %%

times = [start + ids[i] - (start % ids[i]) for i in range(len(ids))]

bi = np.argmin(times)

b_id = ids[bi]

b_id * (min(times)- start)

# %%
start = int(X[0])
ids = [int(x) for x in X[1].split(',') if x != 'x']
id_ts = [(int(x), i) for i, x in enumerate(X[1].split(',')) if x != 'x']


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

a_s = [(-i) % x for x, i in id_ts]

res = chinese_remainder(ids, a_s)

# %%
puzzle.answer_b = res
# %%
