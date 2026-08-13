#!/usr/bin/env python3

debug_mode = False
def p(*var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", *var)

N = int(input())
A = list(map(int, input().split()))
P = list(range(1, N + 1))

possible = True
counts = [0] * N
used = []

for a in A:
    if a != -1:
        if A.count(a) >= 2:
            possible = False
            break
        else:
            used.append(a)

to_use = set(list(range(1, N + 1))) - set(used) - set([-1])

result = []
for a in A:
    if a == -1:
        result.append(to_use.pop())
    else:
        result.append(a)

if not possible:
    print("No")
else:
    print("Yes")
    print(*result)
