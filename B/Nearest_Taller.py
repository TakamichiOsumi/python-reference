#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

cur_max = -1
for idx, a in enumerate(A):
    found = False
    for b in range(idx - 1, -1, -1):
        if A[b] > A[idx]:
            print(b + 1)
            found = True
            break
    
    if not found:
        print(-1)
