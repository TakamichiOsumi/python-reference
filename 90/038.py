#!/usr/bin/env python3

import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))

accum = list(itertools.accumulate(A))

accum.insert(0, 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(accum[r] - accum[l - 1])
