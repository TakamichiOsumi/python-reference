#!/usr/bin/env python3

debug = False # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

H, W, N = map(int, input().split())
area = []
results = []
for _ in range(H):
    area.append([0] * W)
    results.append([0] * W)

p(area)

for _ in range(N):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a - 1, b - 1, c - 1, d - 1
    area[a][b] += 1
    if d + 1 < W and c + 1 < H: # ... [3]
        area[c + 1][d + 1] += 1
    if d + 1 < W: # ... [3]
        area[a][d + 1] -= 1
    if c + 1 < H: # ... [3]
        area[c + 1][b] -= 1

# Horizontal cumulative sum.
for i in range(H):
    cnt = 0
    for j in range(W):
        cnt += area[i][j]
        results[i][j] += cnt

p(results)

# Vertical cumulative sum.
for j in range(W):
    total = 0
    p("WIP : j=", j, results)
    for i in range(H):
        results[i][j] += total
        total = results[i][j] # ... [2]

# Print the results.
for i in range(H):
    print(*results[i])
