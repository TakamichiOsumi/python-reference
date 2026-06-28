#!/usr/bin/env python3

X, Y = map(int, input().split())

if (X % 16) == (Y % 9):
    print("Yes")
else:
    print("No")
