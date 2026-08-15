#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet
from collections import deque, Counter
# import itertools

debug_mode = True
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

N = int(input())
A = SortedList(list(map(int, input().split())))
A.add(0)
cur_idx = A.index(0)

costs = 0

while len(A) > 1:

    center = A[cur_idx]
    if cur_idx == 0:
        next_center_val = A[cur_idx + 1]
        costs += abs(center - A[cur_idx + 1])
        A.remove(center)
        cur_idx = A.index(next_center_val)

    elif cur_idx == len(A) - 1:
        next_center_val = A[cur_idx - 1]
        costs += abs(center - A[cur_idx - 1])
        A.remove(center)
        cur_idx = A.index(next_center_val)
    else:
        left_cost = right_cost = None
        
        left_cost = abs(A[cur_idx - 1] - center)
        right_cost = abs(A[cur_idx + 1] - center)
        if left_cost == right_cost:
            next_center_val = A[cur_idx - 1]
            costs += abs(center - A[cur_idx - 1])
            A.remove(center)
            cur_idx = A.index(next_center_val)
        else:
            if left_cost > right_cost:
                next_center_val = A[cur_idx + 1]
                costs += right_cost
                A.remove(center)
                cur_idx = A.index(next_center_val)
            else:
                next_center_val = A[cur_idx - 1]
                costs += left_cost
                A.remove(center)
                cur_idx = A.index(next_center_val)
    #p("cur costs=", costs, ", list=", A)

print(costs)
