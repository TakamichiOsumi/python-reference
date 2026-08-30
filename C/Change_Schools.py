#!/usr/bin/env python3

from sortedcontainers import SortedDict
from sortedcontainers import SortedList
from collections import Counter

K, N = map(int, input().split())
A = SortedDict(Counter(list(map(int, input().split()))))

class_num = [0] * K
max_num = 0
for a in A:
    class_num[a - 1] += A[a]
    max_num = max(max_num, A[a])

if N == 1:
    print(1)
else:
    added = 0
    for a in A:
        if (A[a] == (max_num - 1)) or (A[a] == max_num):
            added += 1
    print(added)
