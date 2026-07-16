#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

# Key Takeaways :
#
# (1) If the problem description is unclear, then read the sample carefully.
#
# (2) Iterating the inner substring whose length is K can be achieved by below.
#     + 1 in the 'len(S) - K + 1' is the start character for the last substring.
#
#     -------------------------------
#     for i in range(len(S) - K + 1):
#         sub = S[i:i+K]
#     -------------------------------

N, K = map(int, input().split())
S = input()

sd = SortedDict()

for i in range(len(S) - K + 1):
    sub = S[i:i+K]

    if sub in sd.keys():
        sd[sub] += 1
    else:
        sd[sub] = 1

max_freq = max(sd.values())
print(max_freq)

ary = []
for k, v in sd.items():
    if max_freq == v:
        ary.append(k)
print(*ary)
