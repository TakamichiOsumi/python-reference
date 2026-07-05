#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

N, Q = map(int, input().split())

A = SortedList(map(int, input().split()))

for _ in range(Q):
    b = int(input())
    idx = A.bisect_left(b)
    if len(A) == idx:
        print(-1)
    else:
        total = 0
        for i in range(len(A)):
            if i == idx:
                total += b
            else:
                total += min(b - 1, A[i])

        print(total)
