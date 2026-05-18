#!/usr/bin/env python3

N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())
for i in range(Q):
    w = input()

    t_count = 0
    a_count = 0
    for j in list(w):
        # Takahashi
        if j in S:
            t_count += 1
        # Aoki
        if j in T:
            a_count += 1

    if t_count == a_count:
        print("Unknown")
    elif t_count >= len(w):
        print("Takahashi")
    elif a_count >= len(w):
        print("Aoki")
    else:
        print("Unknown")
