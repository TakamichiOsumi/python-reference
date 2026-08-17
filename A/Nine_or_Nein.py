#!/usr/bin/env python3

A, B = map(int, input().split())

if A + B == 9 or A - B == 9 or A * B == 9 or A / B == 9:
    print("Nine")
else:
    print("Nein")
