#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Do not consume the time for "time-consuming" fruitless implementation
#     which apparently cannot achieve the time limitation and leads to the TLE.

from sortedcontainers import SortedList

N, M = map(int, input().split())
menus = []
for i in range(M):
    K, *A = list(map(int, input().split()))
    menu = set(A)
    menus.append(menu)
B = list(map(int, input().split()))

# Reveal the dates by which ingredients will be allowed to be used.
ingredient_open_day = {}
for i in range(len(B)):
    ingredient_open_day[B[i]] = i # Start from 0, 1, ... len(B) - 1

# Fetch the max required days for each menu.
days_menu = { }
for menu in menus:
    # This below code is more time-consuming than the simple call of max function.
    # longest_day = max(SortedList([ingredient_open_day.get(m) for m in menu])) + 1

    longest_day = max([ingredient_open_day.get(m) for m in menu]) + 1

    # Sort out the max required days per each day.
    if longest_day in days_menu.keys():
        days_menu[longest_day] += 1
    else:
        days_menu[longest_day] = 1

# Print the final result.
total_count = 0
for i in range(1, len(B) + 1):
    if i in days_menu.keys():
        total_count += days_menu[i]
    print(total_count)
