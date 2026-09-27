#!/usr/bin/env python3

# Warning : This code does not lead to 'AC'.

from sortedcontainers import SortedList
import itertools
import re

debug = False # debug point
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

Q = int(input())
S = input()
T = input()

# Store all of the start indices of 'T' string in 'hits'.
hits = SortedList([])
for m in re.finditer(T, S):
    hits.add(m.start(0))

p("hits=", hits)
for _ in range(Q):
    l, r = map(int, input().split())
    left_edge, right_edge = l - 1, r - 1

    # The main logic checks whether or not
    # 'left_edge' <= start index for the substring 'T' and len(T) <= 'right edge'.
    # There can be a number same as 'left_edge'.
    if left_edge in hits:
        if left_edge + len(T) - 1 <= right_edge:
            print("Yes")
        else:
            print("No")
        continue

    # Find the smaller and closest index to the 'left index'.
    left_range_to_be_inserted = hits.bisect_left(left_edge)

    # Exclude the failure case where left_edge is bigger than
    # any other indexes in 'hits'. This means there is no substring that exists
    # in the right side string from 'left_range_to_be_inserted'.
    if (left_range_to_be_inserted < len(hits)):
        right_T_start_index = hits[left_range_to_be_inserted]
        if (left_edge <= right_T_start_index) and (right_T_start_index + len(T) - 1 <= right_edge):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
