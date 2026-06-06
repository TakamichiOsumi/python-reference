#!/usr/bin/env python3

from collections import deque

N, M = map(int, input().split())
A = deque(list(map(int, input().split())))

cnt = 0
required = set(list(range(1, M + 1)))
while True:
    set_a = set(A)
    common = set_a & required
    if len(common) < len(required):
       break
    cnt += 1
    A.pop()

print(cnt)
