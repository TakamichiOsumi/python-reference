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
# from collections import deque
# import itertools
# import numpy
# import re

N = int(input())
N, M = map(int, input().split())
S = [ input() for _ in range(N) ]
X_Y = [ list(map(int, input().split())) for _ in range(N) ]

H, W = map(int, input().split())
# C-l C-y r : yas-reload-all
# ij<TAB> : double-loop

count = 0
print(count)

if True:
    print("Yes")
else:
    print("No")
