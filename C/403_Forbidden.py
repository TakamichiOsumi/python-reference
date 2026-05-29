#!/usr/bin/env python3

from sortedcontainers import SortedSet

N, M, Q= map(int, input().split())

user_view = [ SortedSet([]) for i in range(N) ]

for _ in range(Q):
    query = list(map(int, input().split()))
    uidx = query[1] - 1
    if query[0] == 1:
        user_view[uidx].add(query[2])
    elif query[0] == 2:
        user_view[uidx].add(0) # All !
    elif query[0] == 3:
        if 0 in user_view[uidx]:
            print("Yes")
        else:
            if query[2] in user_view[uidx]:
                print("Yes")
            else:
                print("No")
