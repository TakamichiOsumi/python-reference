#!/usr/bin/env python3

from collections import deque, Counter

N = int(input())
strings = [ input().lower() for _ in range(N) ]

c = Counter(strings)

max_val = max(c.values())
print(max_val)
