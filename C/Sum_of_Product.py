#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

total = sum(A) - A[0]

ans = 0
for i in range(N - 1):
    ans += (A[i] * total)
    total -= A[i + 1]

print(ans)


