#!/bin/python

N, A, B = map(int, input().split())

total = 0

for i in range(1, N + 1):
    val = sum(map(int, list(str(i))))
    if val >= A and val <= B:
        total = total + i

print(total)
