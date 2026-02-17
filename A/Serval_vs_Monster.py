#!/usr/bin/env python3

H, A = map(int, input().split())

c = int(H / A)
if H % A == 0:
    print(c)
else:
    print(c + 1)
