#!/usr/bin/env python3

from sortedcontainers import SortedDict
from sortedcontainers import SortedList

debug = True # switch
def p(*var):
    global debug
    if debug:
        if type(var[0]) == type([]):
            print("DEBUG : array:")
            for i in range(len(var[0])):
                print("\t", end = "")
                print(i, var[0][i])
        else:
            print("DEBUG:", *var)

N, S = map(int, input().split())
A = SortedList(map(int, input().split()))
# Append any unrelated value to A, to make the number
# of stored values aligned with N + 1.
A.add(-1)

# Iterate from '0'th card to 'N'th card. (N + 1 times in total.)
# Also, do the same for S range, that is, from '0' to 'S'. (S + 1 in total)
#
# This description leads to a matrix that made of N + 1 rows and S + 1 columns.
dp = [[False] * (S + 1) for _ in range(N + 1) ]
dp[0][0] = True

for card_idx in range(N + 1):
    card_no = A[card_idx]
    p("card_idx=", card_idx, "=> val:", card_no)
    for val in range(S + 1):
        if val == card_no:
            dp[card_idx][card_no] = True
        if card_idx - 1 >= 0:
            # Inherit the upper row's value if it's True.
            if dp[card_idx - 1][val]:
                dp[card_idx][val] = True

            # The core logic works here.
            #
            # When passing by the current 'val' during S's iteration,
            # if the upper line's 'val - card_no' value is True, then
            # it menas the current 'val' can be made as a sigle combination,
            # by adding the current 'val' to the previous 'val - card_no'.
            #
            # This is like offsetting each other and leaving (creating)
            # the current 'card_no'.
            if (val - card_no >= 0) and dp[card_idx - 1][val - card_no]:
                dp[card_idx][val] = True
    p("made matrix:")
    p(dp)

print("Yes" if dp[N][S] else "No")
