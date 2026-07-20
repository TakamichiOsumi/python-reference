#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

A, B, X = map(int, input().split())

# When X cannot afford to buy integer '1', print zero and exit.
if A + B > X:
    print(0)
    exit()

cur_left = 1
cur_right = 10 ** 9

while (cur_right - cur_left) > 1:

    mid = (cur_right + cur_left) // 2
    cur_price = (A * mid) + (B * len(str(mid)))

    if cur_price > X:
        cur_right = mid
    elif cur_price <= X:
        # "<=" (not "<") means the left part is intended to contain
        # acceptable integers.
        cur_left= mid

if cur_right == cur_left:
    print(cur_right)
else:
    left_price = A * cur_left + B * len(str(cur_left))
    right_price = A * cur_right + B * len(str(cur_right))
    if right_price > X:
        print(cur_left)
    elif right_price == X:
        print(cur_right)
    else:
        print(cur_right)
