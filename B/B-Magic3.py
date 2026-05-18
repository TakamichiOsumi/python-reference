#!/usr/bin/env python3

N, S, D = map(int, input().split())

damage = False
for i in range(N):
    x, y = map(int, input().split())
    if x >= S:
        continue

    if y <= D:
        continue

    damage = True

if damage:
    print("Yes")
else:
    print("No")
