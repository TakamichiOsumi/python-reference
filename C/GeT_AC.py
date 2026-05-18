#!/usr/bin/env python3

import re

N, Q = map(int, input().split())
S = input()

found_indexes = [m.span() for m in re.finditer('AC', S)]

pair_pointer = 0
prefix_sum = [0] * N

accumulated_value = 0
for i in range(N):

    # Make sure the pointer to the indexes never exceed the len(found_indexes) - 1,
    # the total number of the finditer() matches.
    #
    # Also, search for the last index of 'AC' to increment accumulated_value.
    if (pair_pointer <= len(found_indexes) - 1) and (i == found_indexes[pair_pointer][1] - 1):
        # Shift the pointer to the next finditer() hit.
        pair_pointer = pair_pointer + 1
        accumulated_value = accumulated_value + 1

    prefix_sum[i] = accumulated_value

for i in range(Q):
     l, r = map(int, input().split())
     l = l - 1
     r = r - 1
     print(prefix_sum[r] - prefix_sum[l])
