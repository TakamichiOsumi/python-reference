#!/usr/bin/env python3

A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
else:
    if A + B >= K:
        print(A)
    else:
        # A + B < K
        C_score = (K - (A + B)) * -1
        print(A + C_score)

