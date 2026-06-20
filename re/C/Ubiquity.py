#!/usr/bin/env python3

N = int(input())

mod = 10 ** 9 + 7

all_numbers = pow(10, N, mod)
no_zero_or_nine = pow(9, N, mod) * 2
both_zero_and_nine = pow(8, N, mod)

print((all_numbers - (no_zero_or_nine - both_zero_and_nine)) % mod)
