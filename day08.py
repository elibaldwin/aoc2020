# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
from collections import Counter, defaultdict
puzzle = Puzzle(year=2020, day=8)
# %%

# %%
X = puzzle.input_data
X = [x.split() for x in X.split('\n')]

seen = set()
accumulator = 0

def acc(i):
  global accumulator
  accumulator += int(X[i][1])
  return i+1

def jmp(i):
  return i + int(X[i][1])

def nop(i):
  return i+1

f_map = {'acc':acc, 'jmp':jmp, 'nop':nop}

def run_code():
  global accumulator, seen
  accumulator = 0
  seen = set()
  ip = 0
  while ip not in seen and ip < len(X):
    seen.add(ip)
    ip = f_map[X[ip][0]](ip)
  return ip >= len(X)

init_t = time.perf_counter()

for i in range(len(X)):
  if X[i][0] == 'jmp':
    X[i][0] = 'nop'
    if run_code():
      break
    X[i][0] = 'jmp'
  elif X[i][0] == 'nop':
    X[i][0] = 'jmp'
    if run_code():
      break
    X[i][0] = 'nop'

print(time.perf_counter() - init_t)
# %%
X = puzzle.input_data
X = [x.split() for x in X.split('\n')]
X = [[x[0], int(x[1])] for x in X]

class bot:
  def __init__(self):
    self.accumulator = 0
    self.fmap = dict()
  
  def reset(self):
    self.accumulator = 0
  
  def run(self, instr):
    if instr[0] not in self.fmap:
      self.fmap[instr[0]] = eval(f'self.{instr[0]}')
    return self.fmap[instr[0]](instr[1:])
  
  def acc(self, arg):
    self.accumulator += arg[0]
    return 1
  
  def jmp(self, arg):
    return arg[0]
  
  def nop(self, arg):
    return 1

def run_bot(b, code):
  b.reset()
  seen = set()
  ip = 0
  while ip not in seen and ip < len(code):
    seen.add(ip)
    ip += b.run(code[ip])
  return ip == len(code)

b = bot()
init_t = time.perf_counter()

for i in range(len(X)):
  if X[i][0] == 'jmp':
    X[i][0] = 'nop'
    if run_bot(b, X):
      break
    X[i][0] = 'jmp'
  elif X[i][0] == 'nop':
    X[i][0] = 'jmp'
    if run_bot(b, X):
      break
    X[i][0] = 'nop'
print(b.accumulator)

print(time.perf_counter() - init_t)
# %%

# %%
