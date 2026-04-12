#!/usr/bin/env python3

A, B, W = map(int, input().split())

min_count = 10 ** 15
max_count = -1

kilo = 1000
for i in range(1, W * kilo + 1):
    if A * i <= W * kilo <= B * i:
        min_count = min(min_count, i)
        max_count = max(max_count, i)

if max_count == -1:
    print("UNSATISFIABLE")
else:
    print(min_count, max_count)
