#!/usr/bin/env python3

# Key Takeaways:
#
# Do not wait the complete result if TLE shows up on the screen.
# When it appears, modify the code as soon as possible.

N, A, B = map(int, input().split())

if N <= A + B:
    if N >= A:
        print(A)
    else:
        print(N)
else:
    pair_count  = N // (A + B)
    left = N - pair_count * (A + B)

    extra = 0
    if left >= A:
        extra = A
    else:
        extra = left

    print(pair_count * A + extra)
