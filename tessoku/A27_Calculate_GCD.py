#!/usr/bin/env python3

# Answer (1). Below code achieves 'AC'.
#
# import math
#
# A, B = map(int, input().split())
#
# print(math.gcd(A, B))

# Answer (2). This also leads to 'AC'.
from sortedcontainers import SortedDict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import numpy
import re

from atcoder.segtree import SegTree
from atcoder.dsu import DSU

import sys

debug = False # switch
def p(*var):
    global debug
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --argument array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)

def get_divisors(N, include_edges = True, include_pair = True):
    if include_edges:
        div = SortedSet([1, N])
    else:
        div = SortedSet([])
    i = 2
    while True:
        if i * i > N:
            break
        if N % i == 0:
            div.add(i)
            if include_pair and N // i != i:
                div.add(N // i)
        i += 1
    return div

A, B = map(int, input().split())
s1 = set(get_divisors(A))
s2 = set(get_divisors(B))
print(max(s1 & s2))
