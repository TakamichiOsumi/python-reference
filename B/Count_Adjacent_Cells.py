#!/usr/bin/env python3

H, W = map(int, input().split())

for i in range(H):
    for j in range(W):
        count = 4
        if i == 0:
            count -= 1
        if j == 0:
            count -= 1
        if i == (H - 1):
            count -= 1
        if j == (W - 1):
            count -= 1
        print(count, "", end="")
        
    print("")
