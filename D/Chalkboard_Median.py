#!/usr/bin/env python3

from sortedcontainers import SortedList

X = int(input())
Q = int(input())

# Main
sl = SortedList([X])
center_idx = 1
for i in range(Q):
    A, B = map(int, input().split())
    sl.add(A)
    sl.add(B)
    print(sl[center_idx])
    center_idx += 1
