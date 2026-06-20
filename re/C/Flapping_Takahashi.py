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
        # If the range between 'l' and 'u' overlap with
        # lh and rh, then the new updated range can be
        # calculated by below.
        lh = max(lh, l)
        rh = min(rh, u)
        # But the range from 'l' to 'u' exists above
        # or below the 'rh' and 'lh', then the next
        # condition becomes True.
        if lh > rh:
            possible = False

    if possible:
        print("Yes")
    else:
        print("No")
