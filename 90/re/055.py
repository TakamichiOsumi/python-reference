#!/usr/bin/env python3

# Key Takeaways:
#
# (1) 1/120 * (N ** 5) can be achieved within 2 seconds.
# (2) Choosing 5 numbers by itertools.combinations leads to MLE.
#     Then, iterating all combinations by for loop is required.

import math
import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(len(A)):
    for j in range(0, i):
        for k in range(0, j):
            for l in range(0, k):
                for m in range(0, l):
                    if A[i] * A[j] * A[k] * A[l] * A[m] % P == Q:
                        cnt += 1
print(cnt)
