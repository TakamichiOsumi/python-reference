#!/usr/bin/env python3

N, M = map(int, input().split())

keys = [ str(i) for i in range(1, M + 1) ]
values = [ [] for _ in range(1, M + 1) ]
d = { k : v for k, v in zip(keys, values) }

for _ in range(N):
    A, B = map(int, input().split())
    d[str(A)].append(B)

for i in range(1, M + 1):
    print(sum(d[str(i)]) / len(d[str(i)]))

