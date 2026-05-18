#!/usr/bin/env python3

H, W, Q = map(int, input().split())

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        R = query[1]
        print(R * W)
        H = H - R
    elif query[0] == 2:
        C = query[1]
        print(C * H)
        W = W - C
