#!/usr/bin/env python3

from sortedcontainers import SortedList
from collections import deque

N = int(input())
A = list(map(int, input().split()))

sA = SortedList(A[0:2])
left = deque(A[2:len(A)])

index = 0
for i in range(N - 2):
    val = left.popleft()
    sA.add(val)
    print(sA[index])
    index += 1
