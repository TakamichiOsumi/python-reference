#!/usr/bin/env python3

from sortedcontainers import SortedList

N = int(input())
A = SortedList(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    X = int(input())
    print(A.bisect_left(X))
