# %%
from aocd.models import Puzzle 
import itertools
from collections import defaultdict
import numpy as np
puzzle = Puzzle(year = 2016, day=23)

# %%
code = [x.split() for x in puzzle.input_data.strip().split('\n')]
registers = defaultdict(int)

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

fn_map = {'cpy':cpy, 'inc':inc, 'dec':dec, 'jnz':jnz, 'tgl':tgl}

registers['a'] = 7
ip = 0
while ip < len(code):
  #print(ip, '\n', code[ip], '\n', registers)
  ip = fn_map[code[ip][0]](ip)
  #input()

registers

# %%
puzzle.answer_a = registers['a']
# %%
code = [x.split() for x in puzzle.input_data.strip().split('\n')]
registers = defaultdict(int)

registers['a'] = 12
ip = 0
inc = 0
while ip < len(code):
  if ip >= 16:
    print(ip)
    print(code[ip])
    print(registers)
    input()
  #print(ip+1, '\n', code[ip], '\n', registers)
  ip = fn_map[code[ip][0]](ip)
  #input()
  inc += 1
  

registers
# %%
