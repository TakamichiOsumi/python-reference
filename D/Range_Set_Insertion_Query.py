#!/usr/bin/env python3

from sortedcontainers import SortedList
from sortedcontainers import SortedSet

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

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

my_buffer = SortedSet([])
extras = SortedList([])

result = []
for i in range(N):
    p("cur my_buffer=", my_buffer,", handle", cumu[i], "with extras", extras)
    for ele in cumu[i]:
        if ele < 0:
            v = -1 * ele
            if v in extras:
                extras.remove(v)
            else:
                my_buffer.remove(v)
        else:
            if ele in my_buffer:
                extras.add(ele)
            else:
                my_buffer.add(ele)
    p("added result=", my_buffer, "with extras=", extras)
    result.append(len(my_buffer))

print(*result)
