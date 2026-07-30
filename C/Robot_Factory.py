#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Define distinctive and clear variable names, for [1] and [2].
#
#     In this problem, 'H''s smallest value is used to search
#     inserted position among 'sorted_B' array, in order to
#     refer to the next (right) 'B''s weight.
#
#     This relationship becomes obvious when index for 'b' is defined
#     as 'b_ins' and 'h_key' like below.
#
# (2) SortedList provides something like leftpop() in the deque, as 'pop(0)'.
#     The order for this function call is O(log(N)) - approximate,
#     explained in https://grantjenks.com/docs/sortedcontainers/sortedlist.html.

from sortedcontainers import SortedList, SortedDict, SortedSet

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
sorted_H = SortedList(H)
B = list(map(int, input().split()))
sorted_B = SortedList(B)

success = True
for i in range(K):

    h_key = sorted_H.pop(0) # ... [1]
    b_ins = sorted_B.bisect_right(h_key) # ... [2]

    if b_ins > (len(sorted_B) - 1):
        if sorted_B[b_ins - 1] >= h_key:
            sorted_B.remove(sorted_B[b_ins - 1])
        else:
            success = False
            break
    else:
        # Remove the counterpart for 'h_key'.
        sorted_B.remove(sorted_B[b_ins])

if success:
    print("Yes")
else:
    print("No")
