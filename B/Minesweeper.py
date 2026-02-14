#!/usr/bin/env python3

def search_around(HW, H, W, h, w):
    count = 0

    if (h - 1 >= 0):
        if (w - 1 >= 0) and HW[h - 1][w - 1] == '#':
            count = count + 1
        if HW[h - 1][w] == '#':
            count = count + 1
        if (w + 1 <= W - 1) and HW[h - 1][w + 1] == '#':
            count = count + 1

    if (w - 1 >= 0) and HW[h][w - 1] == '#':
        count = count + 1
    if HW[h][w]:
        pass
    if (w + 1 <= W - 1) and HW[h][w + 1] == '#':
        count = count + 1

    if (h + 1 <= H - 1):
        if (w - 1 >= 0) and HW[h + 1][w - 1] == '#':
            count = count + 1
        if HW[h + 1][w] == '#':
            count = count + 1
        if (w + 1 <= W - 1) and HW[h + 1][w + 1] == '#':
            count = count + 1
    
    return count

H, W = map(int, input().split())

HW = []
for i in range(0, H):
    HW.append(list(input()))
for h in range(0, H):
    for w in range(0, W):
        if HW[h][w] == '.':
            num = search_around(HW, H, W, h, w)
            HW[h][w] = str(num)

for i in range(0, H):
    print(''.join(HW[i]))
