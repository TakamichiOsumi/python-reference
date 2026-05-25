#!/usr/bin/env python3

# Notes of emacs key-bindings
#
# C-l r : kill-region
# C-l w : kill word from the cursor position
# C-l a : kill until the beginning of line
# C-l e : kill until the end of line
# C-l u : kill until the end of the buffer
# C-l C-m : comment-or-uncomment-region

# from sortedcontainers import SortedList
from collections import deque
# import itertools
# import numpy
# import re

debug_mode = True
def p(var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", var)

Q = int(input())
cards = deque([])
for _ in range(Q):
    t, x = map(int, input().split())
    # left : top
    # right : bottom
    if t == 1:
        cards.appendleft(x)
    elif t == 2:
        cards.append(x)
    elif t == 3:
        print(cards[x - 1])
