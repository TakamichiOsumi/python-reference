#!/usr/bin/env python3

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

val = 0
for i in range(N):
    val = val + (A[i] * B[i])

if val == 0:
    print("Yes")
else:
    print("No")
