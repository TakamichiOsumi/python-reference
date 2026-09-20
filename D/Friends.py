#!/usr/bin/env python3

from atcoder.dsu import DSU

N, M = map(int, input().split())

uf = DSU(N)

for i in range(M):
    N, M = map(int, input().split())
    N, M = N - 1, M - 1
    uf.merge(N, M)

print(max([ len(g) for g in uf.groups() ]))
