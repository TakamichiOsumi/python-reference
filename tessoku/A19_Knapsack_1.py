#!/usr/bin/env python3

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

debug = True # switch
def p(*var):
    global debug
    if debug:
        if type(var[0]) == type([]):
            print("DEBUG : dump array:")
            for i in range(len(var[0])):
                print("\t", end = "")
                print(i, var[0][i])
        else:
            print("DEBUG:", *var)

N, W = map(int, input().split())
w_v = [ list(map(int, input().split())) for _ in range(N) ]
w_v.insert(0, [0, 0])
p(w_v)

value_matrix = [ [0] * (W + 1) for _ in range(N + 1) ]
p(value_matrix)

for item_idx in range(1, N + 1):
    item_weight, item_value = w_v[item_idx][0], w_v[item_idx][1]
    for cur_weight in range(W + 1):
        if cur_weight == item_weight:
            value_matrix[item_idx][cur_weight] = item_value
        if item_idx - 1 >= 0:
            # Upper row exists.
            if value_matrix[item_idx - 1][cur_weight] != 0:
                # Inherit the value of the upper row.
                value_matrix[item_idx][cur_weight] = value_matrix[item_idx - 1][cur_weight]

            if cur_weight - item_weight >= 0 and value_matrix[item_idx - 1][cur_weight - item_weight] != 0:
                possible_value = value_matrix[item_idx - 1][cur_weight - item_weight] + item_value
                value_matrix[item_idx][cur_weight] = max(value_matrix[item_idx][cur_weight], possible_value)
    p(value_matrix)

print(max(value_matrix[N]))
