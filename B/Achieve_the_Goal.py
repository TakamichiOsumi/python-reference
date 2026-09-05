#!/usr/bin/env python3

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

val = N * M - sum(A)
if val > K:
    print(-1)
else:
    print(max(0, val))
