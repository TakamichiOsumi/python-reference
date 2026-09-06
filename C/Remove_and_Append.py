#!/usr/bin/env python3

# Key Takeaways:
#
# Taking memories of two arrays whose sizes are,
# (1) N + 1, where N is from 1 to 2 * (10 ** 5), and
# (2) N + 1 + Q, where N and Q are same as above N.
# doesn't cause MLE.

from collections import deque

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N, Q = map(int, input().split())
P = deque(list(map(int, input().split())))

indexes = [-1] * (N + 1)
active = [False] * (N + 1 + Q)

for i in range(N):
    indexes[P[i]] = i
    active[i] = True
active[N] = True

for i in range(Q):
    a = int(input())
    removed_idx = indexes[a]
    active[removed_idx] = False
    P.append(a)
    active[len(P)] = True
    indexes[a] = len(P) - 1

for i in range(len(P)):
    if (active[i] is True):
        if (i <= len(P) - 1):
            print(P[i], end=" ")
        else:
            print(P[i], end="")
print("")
