#!/usr/bin/env python3

from sortedcontainers import SortedList

val = list(input())

SortedHistory = SortedList([])
is_happy_number = False

while True:
    if len(val) == 1 and val[0] == "1":
        is_happy_number = True
        break

    val = sum([i * i for i in list(map(int, val))])

    if val in SortedHistory:
        break
    SortedHistory.add(val)

    val = list(str(val))

if is_happy_number:
    print("Yes")
else:
    print("No")
