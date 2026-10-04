#!/usr/bin/env python3

from sortedcontainers import SortedList
from sortedcontainers import SortedSet

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

# The basic concept of the approach is to
# handle "Li, Ri, X" as "addition of X from Li index and remove X from Ri + 1
# index", based on the cumulative sum technique.
# Multiplying X by -1 becomes the flag X to be removed.
#
# Same values might be added on the main set variable 'main_set'.
# Then, save the unique members in the set, while saving all overflowing
# 'X's in other SortedList 'extras' and check the existence for 'X'
# whenever adding or removing X from 'main_set' or 'extras'.
#
# 'extras' allows duplicate values.
#
# Print the saved length of 'main_set' by each iteration of 1~N becomes
# the asnwer, number of length for each Si.

N, Q = map(int, input().split())

queries = []
for i in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)

p(queries)

cumu = []
for i in range(N):
    cumu.append([])

for q in queries:
    l, r, x = q
    l, r = l - 1, r - 1
    cumu[l].append(x)
    if (r + 1) <= N - 1:
        cumu[r + 1].append(-1 * x)
    p(q, "=>", cumu)

main_set = SortedSet([])
extras = SortedList([])

result = []
for i in range(N):
    p("cur main_set=", main_set,", handle", cumu[i], "with extras", extras)
    for ele in cumu[i]:
        if ele < 0:
            v = -1 * ele
            if v in extras:
                extras.remove(v)
            else:
                main_set.remove(v)
        else:
            if ele in main_set:
                extras.add(ele)
            else:
                main_set.add(ele)
    p("added result=", main_set, "with extras=", extras)
    result.append(len(main_set))

print(*result)
