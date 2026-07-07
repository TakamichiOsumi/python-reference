#!/usr/bin/env python3

X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

equipped = [0] * len(W)
for _ in range(Q):
    
    P = int(input())

    if equipped[P - 1] == 0:
        equipped[P - 1] = W[P - 1]
    else:
        equipped[P - 1] = 0

    print(X + sum(equipped))
