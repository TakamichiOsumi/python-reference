#!/usr/bin/env python3

N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

diffs = [ P[i] - P[0] for i in range(1, N) ]

if max(diffs) < 0:
    print(0)
else:
    print(max(diffs) + 1)
