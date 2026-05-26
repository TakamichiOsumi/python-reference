#!/usr/bin/env python3

from sortedcontainers import SortedList

N = int(input())
A = SortedList(map(int, input().split()))
Q = int(input())
for i in range(Q):
    min_val = 10 ** 20
    score = int(input())
    A.add(score)
    # Main
    pos = A.index(score)
    if len(A) - 1 >= pos + 1:
        min_val = min(abs(A[pos + 1] - A[pos]), min_val)
    if pos - 1 >= 0:
        min_val = min(abs(A[pos] - A[pos - 1]), min_val)
    print(min_val)
    A.discard(score)
