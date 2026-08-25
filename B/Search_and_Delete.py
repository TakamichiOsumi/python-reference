#!/usr/bin/env python3

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for b in B:
    if A.count(b) >= 1:
        A.remove(b)

print(*A)
