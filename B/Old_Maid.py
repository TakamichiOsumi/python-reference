#!/usr/bin/env python3

from collections import Counter

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
B = list(map(int, input().split()))
c = Counter(B)
# print(c)

ans = 0
for k in c.keys():
    if c[k] >= 2:
        no = (c[k] % 2)
        ans += (k * no)
    elif c[k] == 1:
        ans += k

print(ans)
