#!/usr/bin/env python3

from fractions import Fraction

N, K = map(int, input().split())
p_ary = list(map(int, input().split()))

def calc_expected_val(p):
    return Fraction(1, 2) * (1 + p)

cumu_ary = [0] * N
total = 0
for i in range(N):
    total += calc_expected_val(p_ary[i])
    cumu_ary[i] = total

for i in range(N - K + 1):
    if i == 0:
        max_val = cumu_ary[i + K - 1]
    else:
        max_val = max(max_val, cumu_ary[i + K - 1] - cumu_ary[i - 1])

print(float(max_val))
