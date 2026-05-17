#!/usr/bin/env python3

Q = int(input())

ary = []
idx = 0
for i in range(Q):
    S = input()
    if S[0] == '1':
        N, Order = map(int, S.split())
        ary.append(Order)
    else:
        print(ary[idx])
        idx += 1
