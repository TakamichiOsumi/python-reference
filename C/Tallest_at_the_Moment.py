#!/usr/bin/env python3

from sortedcontainers import SortedSet, SortedList, SortedDict
# from collections import deque
# import itertools
# import numpy
# import re

N = int(input())

H_L = []
sorted_heights = SortedList([ ])
for i in range(N):
    H, L = map(int, input().split())
    H_L.append([H, L])
    sorted_heights.add(H)

H_L.sort(key = (lambda H_L : H_L[1]))

Q = int(input())
T = list(map(int, input().split()))
sorted_T = sorted(T)
i = 0

ans_dict = { }
for t in sorted_T:

    while True:
        if H_L[i][1] > t:
            break
        else:
            sorted_heights.remove(H_L[i][0])
            i += 1

    ans_dict[t] = sorted_heights[-1]

for t in T:
    print(ans_dict[t])
