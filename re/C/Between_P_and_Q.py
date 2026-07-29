#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Estimate the amount of calculations more flexibly.
#     This problem can be solved by simple loop and check.
#     10! = 3628800 is bigger than 10 ** 6, but it's acceptable.
#
# (2) Even if 'NQ' is smaller than 'NP',
#     there are cases where answer is not zero.
#     See the reason in the (4).
#
# (3) Two lists can be compared by list1 < list2 quickly.
#     Comparing list1 < list2 doesn't lead to TLE.
#
# (4) 'NP < num_l < NQ' leads to WA,
#     while 'P < list(l) < Q' leads to AC.
#
#     The reason is, comparing values converted by
#     make_num logic is different from the operation on
#     values from integer arrays. See below.
#
#     'make_num([1, 2, 10]) < make_num([1, 10, 2])'
#     returns False.
#     But, '[1, 2, 10] < [1, 10, 2]'
#     returns True.
#
#     The direct cause of this is the number '10' shifts
#     the order of digits. Also, comparing two lists
#     applies the comparison from the left and returns
#     the boolean result, when the relashionship is decided.
#     >>> [1, 2, 11] < [1, 10, 2]
#     True

import itertools

# *NEVER USED* in the main logic.
def make_num(ary):
    return int("".join(map(str, ary)))

N = int(input())
P = list(map(int, input().split()))
# NP = make_num(P)
Q = list(map(int, input().split()))
# NQ = make_num(Q)

if Q < P: # Not 'NQ < NP' !
    print(0)
    exit()

ans = 0
all_l = list(itertools.permutations(list(range(1, N + 1))))
for l in all_l:
    if P < list(l) < Q:
        ans += 1
print(ans)
