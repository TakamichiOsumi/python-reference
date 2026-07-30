#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Apply -1 to the appended index at [1],
#     since the input A are +1 indexes.
#     Restore the minused indexes, at [2].

N = int(input())

P_and_Gift_From = []
for i in range(N):
    P_and_Gift_From.append([])

for i in range(N):
    K, *A = list(map(int, input().split()))
    for a in A:
        P_and_Gift_From[a - 1].append(i) # ... [1]

for i in range(N):
    no = len(P_and_Gift_From[i])
    ary = sorted(P_and_Gift_From[i])
    new = []
    for a in ary:
        new.append(a + 1) # ... [2]
    print(no, *new)
