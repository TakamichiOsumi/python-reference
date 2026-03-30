#!/usr/bin/env python3

N, M = map(int, input().split())

if N % 2 == 0:
    if N // 2 >= M:
        print("Yes")
    else:
        print("No")
else:
    if N // 2 + 1 >= M:
        print("Yes")
    else:
        print("No")
