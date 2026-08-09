#!/usr/bin/env python3

from collections import deque, Counter

N = int(input())
C = list(map(int, input().split()))

c = Counter(C)
values = c.values()
if len(values) == 1:
    print(0)
    exit()

print(N - max(values))


