#!/usr/bin/env python3

# Key Takeaways:
#
# Adding a new element by O(logN) is acceptable for query = 1.
#
# The main point for this problem is *how to avoid updating each
# battery charged values based on elapsed time*.
#
# This can be skipped when all battery values are converted to
# battery values where the time is equal to 0 and saved in a
# sorted list. Then, printing the biggest value with the time
# of query = 2.

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
