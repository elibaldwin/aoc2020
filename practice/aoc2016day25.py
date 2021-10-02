# %%
from aocd.models import Puzzle 
import itertools
from collections import defaultdict, deque
import numpy as np
puzzle = Puzzle(year = 2016, day=25)

# %%
code = [x.split() for x in puzzle.input_data.strip().split('\n')]
registers = defaultdict(int)
out_buf = []

def get(id):
  global registers
  if id.isalpha():
    return registers[id]
  else:
    return int(id)

def cpy(i):
  global registers, code
  if not code[i][2].isalpha():
    return i+1 # invalide instruction; skip
  registers[code[i][2]] = get(code[i][1])
  return i+1

def inc(i):
  global registers, code
  registers[code[i][1]] += 1
  return i+1

def dec(i):
  global registers, code
  registers[code[i][1]] -= 1
  return i+1

def jnz(i):
  global registers, code
  return i + get(code[i][2]) if get(code[i][1]) else i+1

tgl_map = {'inc':'dec', 'dec':'inc', 'jnz':'cpy', 'cpy':'jnz', 'tgl':'inc'}

def tgl(i):
  global registers, code, tgl_map
  offset = get(code[i][1])
  if 0 <= i+offset < len(code):
    code[i+offset][0] = tgl_map[code[i+offset][0]]
  return i+1

def out(i):
  global registers, code, out_buf
  out_buf.append(get(code[i][1]))
  return i+1

fn_map = {'cpy':cpy, 'inc':inc, 'dec':dec, 'jnz':jnz, 'tgl':tgl, 'out':out}

for a in range(1000):
  registers.clear()
  out_buf.clear()
  registers['a'] = a
  ip = 0
  sig = 0
  while len(out_buf) < 20:
    instr = code[ip][0]
    ip = fn_map[code[ip][0]](ip)
    if instr == 'out':
      if out_buf[-1] != sig:
        break
      sig = (sig+1)%2
  if len(out_buf) > 10:
    print("a = ", a)
    print("output: ", out_buf)
# %%
