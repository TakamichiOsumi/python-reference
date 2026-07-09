#!/usr/bin/env python3

N, M = map(int, input().split())

S = [ list(input()) for _ in range(N) ]

if N == M:
    print(1)
    exit()

pairs = []
for i in range(N - (M - 1)):
    for j in range(N - (M - 1)):
        l = []
        for ver in range(M):
            for hori in range(M):
                l.append(S[i + ver][j + hori])

        pairs.append(tuple(l))

print(len(set(pairs)))

