#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

N, K, M = map(int, input().split())

C_V = SortedDict()
for i in range(N):
    C, V = map(int, input().split())
    if C in C_V.keys():
        C_V[C].add(V)
    else:
        C_V[C] = SortedList([V])

# Key Takeaways:
#
# Remembering value => index where value
# can contain duplicate (same) values
# can't be expressed as dictionary.
# NG : { Value 500 => 1st Color,
#        Value 500 => 2nd Color }.
#
# To address this, consider a tuple
# to make pair of (Color, Max Value)
# and store all of the pairs in this format.
# This can be sorted and works to remember
# each index.
max_group = []
for key in C_V.keys():
    v = C_V[key][len(C_V[key]) - 1]
    max_group.append((key, v))

max_group.sort(key = (lambda max_group : max_group[1]), reverse = True)

decided = [ max_group[i] for i in range(M) ]

for tup in decided:
    C_V[tup[0]].pop()

left = []
for key in C_V.keys():
    left.extend(C_V[key])

part_A = [ decided[i][1] for i in range(len(decided)) ]
part_B = sorted(left, reverse = True)[:(K - M)]

print(sum((part_A)) + sum(part_B))
