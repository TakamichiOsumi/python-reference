#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque, Counter
# import itertools
# import numpy
# import re

debug_mode = False
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

S = input()
N = int(input())
N, M = map(int, input().split())
X_Y = [ list(map(int, input().split())) for _ in range(N) ]
# Ascending order by each 0th element.
sorted_X_Y = sorted(X_Y, reverse = False, key = lambda x : x[0])
strings = [ input() for _ in range(N) ]
chars  = list(input())

# Notes of emacs key-bindings
#
# C-l k : kill-region
# C-l w : kill word from the cursor position
# C-l a : kill until the beginning of line
# C-l e : kill until the end of line
# C-l u : kill until the end of the buffer
# C-l C-m : comment-or-uncomment-region

# Notes of yasnippets
#
# debug_mode<TAB> : Set up 'p' function for debug.
# ij<TAB> : expand double-loop with i and j variable.
# ifelse<TAB> : expand 'if' and 'else' pair.
# ifelif<TAB> : expand 'if','elif' and 'else' set.
