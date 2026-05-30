#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet
from collections import deque

N, M = map(int, input().split())
A = deque(SortedList(list(map(int, input().split()))))
B = deque(SortedList(list(map(int, input().split()))))

# debug
# print(A)
# print(B)

cnt = 0
while len(A) != 0 and len(B) != 0:

    a = A.popleft()
    b = B.popleft()

    while True:
        if b <= a * 2:
            cnt += 1
            break
        else:
            # didn't match !
            if len(A) == 0:
                break
            else:
                a = A.popleft()

print(cnt)

