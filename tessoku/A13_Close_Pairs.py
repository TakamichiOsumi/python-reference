#!/usr/bin/env python3

from sortedcontainers import SortedList

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N, K = map(int, input().split())
A = SortedList(map(int, input().split()))
p(A)

leftmost_idx = A.bisect_right(K)

total = 0
for i in range(N):
    rightmost_idx = A.bisect_right(A[i] + K)

    if rightmost_idx - 1 > i:
        total += ((rightmost_idx - 1) - i)
        
print(total)
