#!/usr/bin/env python3

H, W, X, Y = map(int, input().split())

# This looks a twisted, misleading explanation.
START_Y = X - 1
START_X = Y - 1

matrix = []
for i in range(H):
    s = input().split()
    matrix.extend(s)

visible = 1

# Go up
y = START_Y
x = START_X
while y > 0:
    if matrix[y - 1][x] == '.':
        visible += 1
        y -= 1
        continue
    break

# Go down
y = START_Y
x = START_X
while y < H - 1:
    if matrix[y + 1][x] == '.':
        visible += 1
        y += 1
        continue
    break

# Go right
y = START_Y
x = START_X
while x < W - 1:
    if matrix[y][x + 1] == '.':
        visible += 1
        x += 1
        continue
    break

# Go left
y = START_Y
x = START_X
while x > 0:
    if matrix[y][x - 1] == '.':
        visible += 1
        x -= 1
        continue
    break

print(visible)
