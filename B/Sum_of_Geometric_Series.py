#!/usr/bin/env python3

N, M = map(int, input().split())

X = 0
for i in range(M + 1):
    X += N ** i

if X > 10 ** 9:
    print("inf")
else:
    print(X)
