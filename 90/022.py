#!/usr/bin/env python3

from math import gcd

Num = list(map(int, input().split()))
Num.sort(reverse = True)

common = gcd(Num[0], Num[1], Num[2])

print((Num[0] // common - 1) + (Num[1] // common - 1) + (Num[2] // common - 1))
