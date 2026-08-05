#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque
# import itertools
# import numpy
# import re

debug_mode = False
def p(var_list):
    global debug_mode
    if not type(var_list) is str:
        return
    if debug_mode:
        split = var_list.split(",")
        split = [ var.replace(" ", "") for var in split if var.replace(" ", "") in globals() ]
        if len(split) == 0:
            return
        print('DEBUG: ', end="")
        for i, var in enumerate(split):
            if i == len(split) - 1:
                print('{} => {}'.format(var, eval(var)))
            else:
                print('{} => {}, '.format(var, eval(var)), end="")

S = input()
N = int(input())
N, M = map(int, input().split())
X_Y = [ list(map(int, input().split())) for _ in range(N) ]
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
