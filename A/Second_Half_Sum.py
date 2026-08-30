#!/usr/bin/env python3

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(N // 2, N):
    total += A[i]
print(total)
