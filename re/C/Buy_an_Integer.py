#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Use 'right' and 'left' vars to control search range.
#
# (2) Check if the integer 1 can be bought at the beginning.
#
# (3) Relearn the purpose and conditions for binary search algorithm.
#
#     The purpose is to find a value or position that satisfies
#     some restrictions, from sorted data quickly.
#
#     Conditions:
#     - The input array are sorted.
#     - The array can be split into two parts, satisfactory range or not.
#     - The middle index item can be used to split the two ranges.

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
