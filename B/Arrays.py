#!/usr/bin/env python3

N = int(input())

a = []
for i in range(N):
    L, *A = map(int, input().split())
    a.append(A)

X, Y = map(int, input().split())

print(a[X - 1][Y - 1])
