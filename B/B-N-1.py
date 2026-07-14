#!/usr/bin/env python3

N, M = map(int, input().split())
A = list(map(int, input().split()))

if (sum(A) - M) in A:
    print("Yes")
else:
    print("No")
