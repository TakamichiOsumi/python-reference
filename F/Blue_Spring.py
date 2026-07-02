#!/usr/bin/env python3

N, D, P = map(int, input().split())

F = list(map(int, input().split()))

sorted_F = sorted(F, reverse = True)

buy = 0
cost = 0
for start in range(0, N, D):
    sub = sorted_F[start : start + D]
    if sum(sub) > P:
        buy += 1
        cost += P
    else:
        cost += sum(sub)


print(cost)
