#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

visited_city  = SortedSet()
visited_route = deque()

cur_idx = 0
visited_city.add(0)
visited_route.append(0)
cur_idx = A[cur_idx] - 1

for _ in range(10 ** 18 + 1):

    visited_city.add(cur_idx)
    visited_route.append(cur_idx)
    K -= 1

    if K == 0:
        print(cur_idx + 1)
        exit()

    next_idx = A[cur_idx] - 1
    if next_idx in visited_city:
        K -= 1
        loop_ini_pos = visited_route.index(next_idx)
        loop_len = len(visited_route) - loop_ini_pos
        shift = K % loop_len
        print(visited_route[loop_ini_pos + shift] + 1)
        exit()

    cur_idx = next_idx
