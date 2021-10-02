# %%
from aocd.models import Puzzle
import numpy as np
import itertools
import time
import math
from opcomp import bot
from collections import Counter, defaultdict, deque
import parse
import functools
puzzle = Puzzle(year=2020, day=22)
# %%
source = puzzle.input_data
#source = open('in22.txt', 'r').read().strip()

deck1, deck2 = [[int(y) for y in x.split('\n')[1:]] for x in source.split('\n\n')]
# %%

d1 = deque(deck1)
d2 = deque(deck2)

def play_round(d1, d2):
  c1 = d1.popleft()
  c2 = d2.popleft()
  winner = d1 if c1 > c2 else d2
  winner.append(max(c1, c2))
  winner.append(min(c1, c2))

def score(deck):
  s = 0
  for i in range(len(deck)):
    s += deck[i] * (len(deck) - i)
  return s

# %%

C = 1

# True: d1 wins, False: d2 wins
def play_round_rec(d1, d2, depth=0):
  c1 = d1[0]
  c2 = d2[0]
  if c1+1 <= len(d1) and c2+1 <= len(d2):
    #print("Playing a sub-game to determine the winner...\n")
    return play_rec(d1[1:c1+1], d2[1:c2+1], depth+1)[0] # d1 wins
  else:
    return c1 > c2

def play_rec(d1, d2, depth=0):
  global C
  S = set()
  game_num = C
  C += 1
  #print("=== Game", game_num, "===")
  rd = 1
  while d1 and d2:
    #print('-- Round ', rd, '(Game', game_num, ') --')
    #print("Player 1's deck:", ', '.join(str(x) for x in d1))
    #print("Player 2's deck:", ', '.join(str(x) for x in d2))
    if (hash(d1), hash(d2)) in S:
      #print("end game", game_num, "(already seen)")
      return (True, score(d1))
    S.add((hash(d1), hash(d2)))
    if play_round_rec(d1, d2, depth):
      #print("Player 1 wins round", rd, "of game", game_num, "!")
      d1 = d1[1:] + d1[:1] + d2[:1]
      d2 = d2[1:]
    else:
      #print("Player 2 wins round", rd, "of game", game_num, "!")
      d2 = d2[1:] + d2[:1] + d1[:1]
      d1 = d1[1:]
    rd += 1
    #print()
  #print("The winner of game", game_num, 'is player', 1 if d1 else 2, '!')
  return (bool(d1), score(d1 if d1 else d2))

# todo: make it work correctly on test case
# then run on real input

# %%
