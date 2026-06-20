#!/usr/bin/env python3

import itertools
import copy

N = int(input())
A = list(map(int, input().split()))

rA = copy.deepcopy(A)
rA.reverse()
rA.insert(0, 0)
rA_acmlt = list(itertools.accumulate(rA))

total = 0
for i in range(0, N):
    total += (A[i] * rA_acmlt[len(rA_acmlt) - (2 + i)])

print(total % (10 ** 9 + 7))
