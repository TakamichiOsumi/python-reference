#!/usr/bin/env python3

N = int(input())
A, B, C = map(int, input().split())

min_val = 10000
for i in range(10000):
    for j in range(10000):
        value = i * A + j * B
        if N < value or (N - value) % C != 0:
            continue
        tmp = i + j + (N - value) // C
        if min_val > tmp:
            min_val = tmp
print(min_val)
