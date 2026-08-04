#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

N, M = map(int, input().split())
A = SortedList(map(int, input().split()))

cp_M = M
while cp_M > 0:
    # main
    max_val = A.pop()
    max_val = int(max_val / 2)
    A.add(max_val)
    cp_M -= 1

print(sum(A))


