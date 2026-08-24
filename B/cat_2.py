#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque, Counter
import itertools
# import numpy
# import re

N = int(input())
strings = [ input() for _ in range(N) ]

pairs = list(itertools.permutations(range(N), 2))

s = set()
for p in pairs:
    s.add(strings[p[0]] + strings[p[1]])

print(len(s))
