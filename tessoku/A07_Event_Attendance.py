#!/usr/bin/env python3

from sortedcontainers import SortedList
from collections import defaultdict

debug = False # debug switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

D = int(input())
N = int(input())
ans = [0] * D

sd = defaultdict(SortedList)
for _ in range(N):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    sd[l].add(r)

p(sd)

cnt = 0
dec_counts = [0] * (D + 1) # D + 1 ... [1]
for i in range(D):
    p("i=", i)
    dec_days = sd[i]
    cnt += len(dec_days)
    for d in dec_days:
        dec_counts[d + 1] += 1 # d + 1 ... [2]
        p("joined!")
    if dec_counts[i] > 0:
        cnt -= dec_counts[i]
        p("left ", dec_counts[i])
    print(cnt)
    p("dec_days:", dec_days)
    p("dec_counts:", dec_counts)
