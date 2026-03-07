#!/usr/bin/env python3

N, X = map(int, input().split())

total = 0
drunken = False
index = -1

for i in range(N):
    V, P = map(int, input().split())

    if V * P + total > X * 100:
        if drunken == True:
            index = i + 1
        break
    else:
        total += V * P

print(index)
