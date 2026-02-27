#!/usr/bin/env python3

H, W, X, Y = map(int, input().split())

# This looks a twisted, misleading swap.
START_Y = X - 1
START_X = Y - 1

matrix = []
for i in range(H):
    s = input().split()
    matrix.extend(s)

visible = 1

# Go up.
y = START_Y
x = START_X
while y > 0: # y should be greater or equal to 1 to be decremented.
    if matrix[y - 1][x] == '.':
        visible += 1
        y -= 1
        continue
    break

# Go down. Reset the position.
y = START_Y
x = START_X
while y < H - 1: # y should be smaller than the last index to be incremented up to the bottom.
    if matrix[y + 1][x] == '.':
        visible += 1
        y += 1
        continue
    break

# Go right. Reset the position.
y = START_Y
x = START_X
while x < W - 1: # x should be smaller than the last index to be incremented to reach the rightmost cell.
    if matrix[y][x + 1] == '.':
        visible += 1
        x += 1
        continue
    break

# Go left. Reset the position.
y = START_Y
x = START_X
while x > 0: # x should be greater or equal to 1 to be decremented.
    if matrix[y][x - 1] == '.':
        visible += 1
        x -= 1
        continue
    break

print(visible)
