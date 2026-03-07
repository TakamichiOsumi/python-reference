#!/usr/bin/env python3

import math

A, B = map(int, input().split())

def gcd(large, small):
    while small:
        large, small = small, large % small

    return large

if A > B:
    large, small = A, B
elif A < B:
    large, small = B, A
else:
    print(A)
    exit()

val = gcd(large, small)
print((large * small // val))
