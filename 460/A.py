#!/usr/bin/env python3

N, M = map(int, input().split())

cnt = 0
while M != 0:

    x = N % M
    M = x

    cnt +=1

print(cnt)
