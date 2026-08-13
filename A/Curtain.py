#!/usr/bin/env python3

A, B = map(int, input().split())

if B * 2 >= A:
    print(0)
else:
    print(A - B * 2)
