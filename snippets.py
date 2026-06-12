#!/usr/bin/env python3

N = int(input())
N, M = map(int, input().split())
Strings = [ input() for _ in range(N) ]
X_Y = [ list(map(int, input().split())) for _ in range(N) ]

# Notes of emacs key-bindings
#
# C-l k : kill-region
# C-l w : kill word from the cursor position
# C-l a : kill until the beginning of line
# C-l e : kill until the end of line
# C-l u : kill until the end of the buffer
# C-l C-m : comment-or-uncomment-region

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque
# import itertools
# import numpy
# import re

# Notes of yasnippets
#
# debug_mode<TAB> : Set up 'p' function for debug.
# ij<TAB> : expand double-loop with i and j variable.
# ifelse<TAB> : expand 'if' and 'else' pair.
# ifelif<TAB> : expand 'if','elif' and 'else' set.
