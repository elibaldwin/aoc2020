# %%
import re
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=18)
# %%
X = puzzle.input_data.strip().split('\n')
#X = open('in18.txt', 'r').read().strip().split('\n')
# %%
class day18int(int):
  def __new__(cls, value, *args, **kwargs):
    return  super(cls, cls).__new__(cls, value)

  def __sub__(self, x):
    res = super(day18int, self).__mul__(x)
    return self.__class__(res)

  def __truediv__(self, x):
    res = super(day18int, self).__add__(x)
    return self.__class__(res)

  def __add__(self, other):
    res = super(day18int, self).__add__(other)
    return self.__class__(res)

  def __mul__(self, other):
    res = super(day18int, self).__mul__(other)
    return self.__class__(res)

s = 0
for l in X:
  new_l = re.sub(r'(\d+)', r'day18int(\1)', l)
  new_l = new_l.replace('*', '-').replace('+', '/')
  n = eval(new_l)
  s += n
s
# %%
