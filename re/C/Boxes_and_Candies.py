#!/usr/bin/env python3

N, x = map(int, input().split())

a = list(map(int, input().split()))
dec_count = 0

if a[0] > x:
    extra = a[0] - x
    dec_count += extra
    a[0] = x

for i in range(0, N - 1):
    if a[i] + a[i + 1] > x:
        extra = a[i] + a[i + 1] - x
        a[i + 1] = a[i + 1] - extra
        dec_count += extra

print(dec_count)
