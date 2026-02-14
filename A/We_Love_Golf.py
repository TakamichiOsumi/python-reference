#!/bin/python


K = int(input())
A, B = map(int, input().split())

base = (A // K) * K
if base == A:
    print("OK")
else:
    if (base + K) <= B:
        print("OK")
    else:
        print("NG")
