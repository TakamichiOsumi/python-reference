#!/usr/bin/env python3

H, W, N = map(int, input().split())

mat = [ set(map(int, input().split())) for _ in range(H) ]

values = set([ int(input()) for _ in range(N) ])

max_count = 0
for i in range(H):
    max_count = max(max_count, len(mat[i] & values))
print(max_count)
