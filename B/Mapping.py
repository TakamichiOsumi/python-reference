#!/usr/bin/env python3

N, M = map(int, input().split())

F = list(map(int, input().split()))

used = [False] * (M + 1)

for i in range(N):
    used[F[i]] = True

if len(F) == len(set(F)):
    print("Yes")
else:
    print("No")

if sum(used) == M:
    print("Yes")
else:
    print("No")
