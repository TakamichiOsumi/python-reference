#!/usr/bin/env python3

N, K = map(int, input().split())

count = 0
for i in range(1, N + 1):
    ary = map(int, list(str(i)))
    if sum(ary) == K:
        count += 1

print(count)
