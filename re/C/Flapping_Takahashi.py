#!/usr/bin/env python3

T = int(input())

for _ in range(T):
    N, H = map(int, input().split())

    lh = rh = H
    now = 0
    possible = True

    for _ in range(N):
        # No need to consider the case when the 'l' is 1,
        # since the 'l' is always greater than or equal to 1.
        t, l, u = map(int, input().split())
        diff_time = t - now
        now = t

        if not possible:
            continue

        lh = lh - diff_time
        rh = rh + diff_time

        # Updated range can be calculated by
        # max(lower possible point, lower limitation point)
        # and
        # min(upper possible point, upper limitation point).
        lh = max(lh, l)
        rh = min(rh, u)
        # If the two types of ranges
        # (1) from 'l' to 'u'
        # (2) from 'lh' to 'rh'
        # don't overlap, then the below condition gets satisfied.
        if lh > rh:
            possible = False

    if possible:
        print("Yes")
    else:
        print("No")
