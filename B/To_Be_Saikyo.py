#!/usr/bin/env python3

# Key Takeawasy:
#
# (1) N can be 1.
# (2) max(-2, -3, -4, -5, -6) returns -2.
#     If 'diffs' are all minus value, it means the 1st person is already strongest.
#     Yet, max(-2, -3, -4, -5, -6) + 1 returns -1 and this is a wrong answer.
#     The answer should be 0 if the 1st person is strong enough from the beginning.
#     This check can be expressed as max(diffs) < 0.

N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

diffs = [ P[i] - P[0] for i in range(1, N) ]

if max(diffs) < 0:
    print(0)
else:
    print(max(diffs) + 1)
