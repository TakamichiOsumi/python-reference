#!/usr/bin/env python3


# Key Takeaways :
#
# (1) This is a typical problem of cumulative sum.
#     But, the way to retrieve the cumulative sum is not straightforward,
#     if the index search is conducted in a simple manner.
#     Padding zero to keep the indexes same between class1 and class2 is
#     the good solution for this.

import itertools

N = int(input())

class1 = [0]
class2 = [0]

for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        class1.append(P)
        class2.append(0)
    elif C == 2:
        class1.append(0)
        class2.append(P)

class1_accum = list(itertools.accumulate(class1))
class2_accum = list(itertools.accumulate(class2))

Query = int(input())
for i in range(Query):
    L, R = map(int, input().split())
    print(class1_accum[R] - class1_accum[L - 1], end="")
    print(" ", end="")
    print(class2_accum[R] - class2_accum[L - 1])
