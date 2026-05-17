#!/usr/bin/env python3

# import pdb

from sortedcontainers import SortedList
# from collections import deque
# import itertools
# import numpy
# import re

X = int(input())
Q = int(input())

# Main
sl = SortedList([X])
center_idx = 1
for i in range(Q):
    A, B = map(int, input().split())
    sl.add(A)
    sl.add(B)
    # print("cur_status =",sl)
    print(sl[center_idx])
    center_idx += 1
