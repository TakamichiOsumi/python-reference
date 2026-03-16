#!/usr/bin/env python3

N = int(input())

def convert_dec_to_n_adic(decimal, n):
    s = ''
    while decimal > 0:
        s = str(decimal % n) + s
        decimal = decimal // n
    return s

print(convert_dec_to_n_adic(N, 2).zfill(10))
