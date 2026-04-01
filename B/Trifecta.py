#!/usr/bin/env python3

N = int(input())
T = list(map(int, input().split()))

replace = 1000
top_three = []
for i in range(3):
    idx = T.index(min(T))
    top_three.append(idx)
    T[idx] = replace

for i in range(3):
    top_three[i] += 1

print(*top_three)
