#!/usr/bin/env python3

import itertools

N = int(input())
A = list(map(int, input().split()))

cnt = 0
for left in range(N - 1):

    for right in range(left, N):
        val = sum([ A[j] for j in range(left, right + 1) ])

        satisfy = True
        for i in range(left, right + 1):
            if val % A[i] == 0:
                satisfy = False
                break

        if satisfy:
            cnt += 1
        
print(cnt)
