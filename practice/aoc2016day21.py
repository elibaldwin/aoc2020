# %%
from aocd.models import Puzzle 
puzzle = Puzzle(year = 2016, day=21)
# %%
X = [x.split() for x in puzzle.input_data.split('\n')]

def swap_pos(pwd, instr):
  x = int(instr[2])
  y = int(instr[5])
  tmp = pwd[x]
  pwd[x] = pwd[y]
  pwd[y] = tmp
  return pwd

def swap_let(pwd, instr):
  x = pwd.index(instr[2])
  y = pwd.index(instr[5])
  tmp = pwd[x]
  pwd[x] = pwd[y]
  pwd[y] = tmp
  return pwd

def swap(pwd, instr):
  return swap_pos(pwd, instr) if instr[1] == 'position' else swap_let(pwd, instr)

def rotate_lr(pwd, d, s):
  if d == 'right':
    s = len(pwd) - (s % len(pwd))
  return pwd[s%len(pwd):] + pwd[:s%len(pwd)]

def rotate(pwd, instr):
  if instr[1] == 'based':
    n = pwd.index(instr[6])
    n += (1 if n < 4 else 2)
    return rotate_lr(pwd, 'right', n)
  else:
    return rotate_lr(pwd, instr[1], int(instr[2]))

def reverse(pwd, instr):
  x = int(instr[2])
  y = int(instr[4])
  head = pwd[:x]
  mid = pwd[x:y+1]
  tail = pwd[y+1:]
  return head + mid[::-1] + tail

def move(pwd, instr):
  x = int(instr[2])
  y = int(instr[5])
  tmp = pwd.pop(x)
  pwd.insert(y, tmp)
  return pwd

fmap = {'swap': swap, 'rotate': rotate, 'reverse': reverse, 'move': move}


# %%
pwd = list('abcdefgh')
for instr in X:
  res = fmap[instr[0]](pwd, instr)
  if len(res) != len(pwd):
    print("error")
    print(pwd)
    print(res)
    print(instr)
  pwd = res
res = ''.join(pwd)
res
# %%
puzzle.answer_a = res
# %%

def r_rotate_lr(pwd, d, s):
  if d == 'left':
    s = len(pwd) - (s % len(pwd))
  return pwd[s%len(pwd):] + pwd[:s%len(pwd)]

def r_rotate(pwd, instr):
  if instr[1] == 'based':
    n = pwd.index(instr[6])
    n += (1 if n < 4 else 2)
    for i in range(1, len(pwd)+5):
      attempt = rotate_lr(pwd.copy(), 'left', i)
      if rotate(attempt, instr) == pwd:
        return attempt
  else:
    return r_rotate_lr(pwd, instr[1], int(instr[2]))

def r_move(pwd, instr):
  x = int(instr[5])
  y = int(instr[2])
  tmp = pwd.pop(x)
  pwd.insert(y, tmp)
  return pwd

fmap = {'swap': swap, 'rotate': r_rotate, 'reverse': reverse, 'move': r_move}

pwd = list('fbgdceah')
for instr in reversed(X):
  pwd = fmap[instr[0]](pwd, instr)
res = ''.join(pwd)
res
# %%
puzzle.answer_b = res
# %%
