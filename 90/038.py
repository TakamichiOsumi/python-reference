#!/usr/bin/env python3

# Key Takeaways:
#
# Each answer can be calculated by
# (the total number until the 'r'th day) - (the total number until the 'l - 1'th day).
#
# Padding 0 to the leftmost index by insert() enables simple reference to accum[r] and
# diff calculation using accum[l - 1] with accum[r].
#
# This logic with 0 is easy to understand, when listing two examples as below.
# (1) The value from the 1st day to Nth day can be calculated by accum[N] (- accum[0]),
#     where accum[0] is zero.
# (2) The value from the 2nd day to Nth day can be calculated by accum[N] - accum[1].

import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))

accum = list(itertools.accumulate(A))

accum.insert(0, 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(accum[r] - accum[l - 1])
