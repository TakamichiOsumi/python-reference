#!/usr/bin/env python3

T, X = map(int, input().split())

A = list(map(int, input().split()))

d = dict()
prev = d["0"] = A[0]
for i in range(1, len(A)):
    if abs(A[i] - prev) >= X:
        prev = d[str(i)] = A[i]
        # print(i, "=>", A[i])

k = list(map(int, list(d.keys())))
k.sort()

for i in k:
    print(str(i), d[str(i)])
