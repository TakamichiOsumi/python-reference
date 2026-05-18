#!/usr/bin/env python3

# import pdb

# from sortedcontainers import SortedList
# from collections import deque
# import itertools
# import numpy
# import re

import copy

N, M = map(int, input().split())

menus = []
for i in range(M):
    K, *A = list(map(int, input().split()))
    menu = set(A)
    menus.append(menu)

B = list(map(int, input().split()))

my_dict = {}
for i in range(len(B)):
    my_dict[B[i]] = i

# print(my_dict)

# Main Logic
#
# Fetch all corresponding required days for each ingredients.
# Get the max required day from this data
days_menu = { }
for menu in menus:
    longest_day = max([my_dict.get(m) for m in menu]) + 1

    # Sort out the required days per each day.
    if longest_day in days_menu.keys():
        days_menu[longest_day] += 1
    else:
        days_menu[longest_day] = 1

# print(days_menu)
total_count = 0
for i in range(1, len(B) + 1):
    if i in days_menu.keys():
        total_count += days_menu[i]
    print(total_count)

