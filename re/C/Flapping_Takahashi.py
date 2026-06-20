#!/usr/bin/env python3

T = int(input())

for _ in range(T):
    N, H = map(int, input().split())

    lower_edge = upper_edge = H
    now = 0
    possible = True

    for _ in range(N):
        # No need to consider the case when the 'allowed_lower_edge' is 1,
        # since the 'allowed_lower_edge' is always greater than or equal to 1.
        t, allowed_lower_edge, allowed_upper_edge = map(int, input().split())
        diff_time = t - now
        now = t

        if not possible:
            continue

        lower_edge = lower_edge - diff_time
        upper_edge = upper_edge + diff_time

        # Updated range can be calculated by
        # max(lower possible point, lower limitation point)
        # and
        # min(upper possible point, upper limitation point).
        lower_edge = max(lower_edge, allowed_lower_edge)
        upper_edge = min(upper_edge, allowed_upper_edge)
        # If and only if the two types of ranges
        # (1) from 'allowed_lower_edge' to 'allowed_upper_edge'
        # (2) from 'lower_edge' to 'upper_edge'
        # don't overlap, then the below condition gets satisfied.
        if lower_edge > upper_edge:
            possible = False

    if possible:
        print("Yes")
    else:
        print("No")
