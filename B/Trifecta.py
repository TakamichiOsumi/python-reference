#!/usr/bin/env python3

N = int(input())
T = list(map(int, input().split()))

replace = 1000
hourses = []
for i in range(3):
    idx = T.index(min(T))
    hourses.append(idx)
    T[idx] = replace

for i in range(3):
    hourses[i] += 1

print(*hourses)
