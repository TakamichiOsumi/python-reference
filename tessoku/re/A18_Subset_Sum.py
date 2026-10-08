#!/usr/bin/env python3

from sortedcontainers import SortedDict
from sortedcontainers import SortedList

def y_or_n(v):
    print("Yes" if v else "No")

debug = True # switch
def p(*var):
    global debug
    if debug:
        if type(var[0]) == type([]):
            print("array print():")
            for v in var[0]:
                print(v)
        else:
            print("DEBUG:", *var)

N, S = map(int, input().split())
A = SortedList(map(int, input().split()))
A.add(-1)

dp = [[False] * (S + 1) for _ in range(N + 1) ]
dp[0][0] = True

for card_idx in range(N + 1):
    card_no = A[card_idx]
    p("card_idx=", card_idx, "=> val:", card_no)
    for val in range(S + 1):
        if val == card_no:
            dp[card_idx][card_no] = True
        if card_idx - 1 >= 0:
            if dp[card_idx - 1][val]:
                dp[card_idx][val] = True
            if (val - card_no >= 0) and dp[card_idx - 1][val - card_no]:
                dp[card_idx][val] = True
    p("made matrix:")
    p(dp)

print("Yes" if dp[N][S] else "No")
