#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque
# import itertools
# import numpy
# import re


N = int(input())

P_and_Gift_From = []
for i in range(N):
    P_and_Gift_From.append([])

for i in range(N):
    K, *A = list(map(int, input().split()))
    for a in A:
        P_and_Gift_From[a - 1].append(i)

for i in range(N):
    no = len(P_and_Gift_From[i])
    ary = sorted(P_and_Gift_From[i])
    new = []
    for a in ary:
        new.append(a +1)
    print(no, *new)
