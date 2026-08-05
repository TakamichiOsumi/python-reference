#!/usr/bin/env python3

# Key Takeaways:
#
# Use simple implementation of logic.
# In this problem, using Counter() to count up each number frequency
# was effective to eliminate bugs.

from collections import Counter

from math import factorial

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

ans = 0
for k, v in C.items():
    if v <= 1:
        continue

    ans += (v * (v - 1) / 2 * (N - v))

print(int(ans))
