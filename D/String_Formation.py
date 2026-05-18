#!/usr/bin/env python3

# Key Takeaways:
#
# (1) List up major collection features and their time complexities.
#     This will help to select ideas to solve the problem.
#     For instance, deque.reverse() requires O(N).
# (2) Choose simple and short names for variables.
#     In the below case, avoid "queries" and use "q" instead.
# (3) Read the problem description *carefully*.
#     Regarding this problem, T == 1 means not deque.rotate()
#     but deque.reverse().

from collections import deque

S = input()
Q = int(input())

d = deque(list(S))

reverse = False
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        reverse = False if reverse else True
    elif q[0] == "2":
        if q[1] == "1":
            if reverse:
                d.append(q[2])
            else:
                d.appendleft(q[2])
        elif q[1] == "2":
            if reverse:
                d.appendleft(q[2])
            else:
                d.append(q[2])

if reverse:
    for i in range(len(d) - 1, -1, -1):
        print(d[i], end="")
else:
    for i in range(len(d)):
        print(d[i], end="")
print("")
