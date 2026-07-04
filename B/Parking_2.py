#!/usr/bin/env python3

X, Y, L, R, A, B = map(int, input().split())

LR_range = set(range(L, R))
parked_range = set(range(A, B))

print(len(LR_range & parked_range) * X + len(parked_range - LR_range) * Y)
