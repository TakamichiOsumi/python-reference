#!/usr/bin/env python3

# from sortedcontainers import SortedDict # keys(), values(), items(), bisect_left(), bisect_right(), etc
# from sortedcontainers import SortedList # add(), bisect_left(), bisect_right(), count(), extend(), index(), insert(index, value), etc
# from sortedcontainers import SortedSet # add(), remove(), etc
# from collections import deque # append(), appendleft(), extend(), extendleft(), index(), pop(), popleft(), etc
# from collections Counter # c = Counter('abcdeabc') # print(''.join(sorted(c.elements()))) => 'aabbccde'
# import itertools # itertools.permutations(range(A, B)), itertools.combinations(range(A, B), C),
#                  # itertools.product(range(A, B), range(C, D)), etc
# import numpy
# import re # for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

S = input()
N = int(input())
N, M = map(int, input().split())
X_Y = [ list(map(int, input().split())) for _ in range(N) ]
# Ascending order by each 0th element.
sorted_X_Y = sorted(X_Y, reverse = False, key = lambda x : x[0])
strings = [ input() for _ in range(N) ]
chars  = list(input())

# Q = int(input())
# for i in range(Q):
#     s = input()
#     if s[0] == '1':
#         # query = 1
#         q, x, y = map(int, s.split())
#     else:
#         # like for query = 2.
# 	q, k = map(int, s.split())

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
# ij<TAB> : expand double-loop with i and j variable.
# ifelse<TAB> : expand 'if' and 'else' pair.
# ifelif<TAB> : expand 'if','elif' and 'else' set.
