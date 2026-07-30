#!/usr/bin/env python3

from sortedcontainers import SortedList, SortedDict, SortedSet

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
sorted_H = SortedList(H)
B = list(map(int, input().split()))
sorted_B = SortedList(B)

success = True
for i in range(K):

    h_key = sorted_H.pop(0)
    b_ins = sorted_B.bisect_right(h_key)

    if b_ins > (len(sorted_B) - 1):
        if sorted_B[b_ins - 1] >= h_key:
            sorted_B.remove(sorted_B[b_ins - 1])
        else:
            success = False
            break
    else:
        # Remove the counterpart for h_key.
        sorted_B.remove(sorted_B[b_ins])

if success:
    print("Yes")
else:
    print("No")
