#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

H, W, N = map(int, input().split())

Row_Garbage = SortedDict()
Column_Garbage = SortedDict()

for _ in range(N):
    x, y = map(int, input().split())

    # x -> y
    if x in Row_Garbage.keys():
        Row_Garbage[x].add(y)
    else:
        Row_Garbage[x] = SortedList([y])

    # y -> x
    if y in Column_Garbage.keys():
        Column_Garbage[y].add(x)
    else:
        Column_Garbage[y] = SortedList([x])

Q = int(input())

for _ in range(Q):
    q, no = map(int, input().split())
    if q == 1:
        if (no in Row_Garbage.keys()) is False:
            print(0)
            continue
        
        removed = Row_Garbage[no]
        print(len(removed))
        for r in list(removed):
            Column_Garbage[r].discard(no)
        Row_Garbage[no] = SortedList([])
    elif q == 2:

        if (no in Column_Garbage.keys()) is False:
            print(0)
            continue
        
        removed = Column_Garbage[no]
        print(len(removed))
        for r in list(removed):
            Row_Garbage[r].discard(no)
        Column_Garbage[no] = SortedList([])

