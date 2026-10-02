#!/usr/bin/env python3

from sortedcontainers import SortedList
import math

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

def cur_prints_excceeded_K(N, A, middle):
    value = 0
    for i in range(N):
        value += (middle // A[i])
    p("cur prints = ", value, " at ", middle, "th day.")

    if value >= K:
        return True
    else:
        return False

N, K = map(int, input().split())
A = SortedList(map(int, input().split()))
smaller_than_K = 0
equal_or_bigger_than_K = 10 ** 9

while equal_or_bigger_than_K > smaller_than_K:

    p("range from", smaller_than_K, "to", equal_or_bigger_than_K)

    middle_boundary = (smaller_than_K + equal_or_bigger_than_K) // 2

    exceeded = cur_prints_excceeded_K(N, A, middle_boundary)

    if exceeded:
        equal_or_bigger_than_K = middle_boundary
    else:
        smaller_than_K = middle_boundary + 1

print(smaller_than_K)
