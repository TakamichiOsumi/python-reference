#!/usr/bin/env python3

N, K = map(int, input().split())

count = 0
while True:
    if K - N <= 0:
        break
    K -= N
    count += 1
    N += 1

print(count)
