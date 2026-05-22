#!/usr/bin/env python3

H, W = map(int, input().split())

width_blocks = W // 2
width_left = W % 2

height_blocks = H // 2
height_left = H % 2

if H == 1 or W == 1:
    print(H * W)
else:
    c = height_blocks * width_blocks
    if height_left == 1 and width_left == 1:
        c += 1
        c += (height_blocks + width_blocks)
    elif width_left == 1:
        c += height_blocks
    elif height_left == 1:
        c += width_blocks
    print(c)
