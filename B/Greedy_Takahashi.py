#!/usr/bin/env python3

A, B, K = map(int, input().split())

if A >= 1:
    if K > A:
        K = K - A
        A = 0
    else:
        # K <= A
        A = A - K
        K = 0

if B >= 1:
    if K > B:
        K = K - B
        B = 0
    else:
        B = B - K
        K = 0

print(A, B)
