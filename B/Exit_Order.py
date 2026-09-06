#!/usr/bin/env python3

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
P = list(map(int, input().split()))
sP = sorted(P, reverse = False)
new_N = [-1] * N

success = True
size = 10
for start in range(0, N, size):
    subP = P[start : start + size]
    sub_sP = sP[start : start + size]
    if set(subP) != set(sub_sP):
        success = False
        break

if success:
    print("Yes")
else:
    print("No")
