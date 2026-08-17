#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

Q, V = map(int, input().split())

battery = SortedList([])

for i in range(Q):
    s = input()
    if s[0] == "1":
        q, t, w = map(int, s.split())
        battery.add(w - t)
    else:
        q, t = map(int, s.split())
        if len(battery) == 0:
            print(-1)
        else:
            max_val = battery[len(battery) - 1]
            print(min(max_val + t, V))
            battery.remove(max_val)
