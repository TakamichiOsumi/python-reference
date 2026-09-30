#!/usr/bin/env python3

from sortedcontainers import SortedList

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N, X = map(int, input().split())
A = SortedList(map(int, input().split()))
p(A)
print(A.bisect_left(X) + 1)
