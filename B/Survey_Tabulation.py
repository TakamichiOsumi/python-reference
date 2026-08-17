#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
from collections import deque, Counter
# import itertools
# import numpy
# import re

debug_mode = False
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

N = int(input())
strings = [ input().lower() for _ in range(N) ]

c = Counter(strings)

max_val = max(c.values())
print(max_val)
