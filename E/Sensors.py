#!/usr/bin/env python3

from collections import deque

H, W = map(int, input().split())

visited = []
for i in range(H):
    visited.append([False] * W)

area = []
for i in range(H):
    l = list(input())
    area.append(l)

censor_blocks = 0

for i in range(H):
    for j in range(W):
        if not visited[i][j]:
            if area[i][j] == '#':
                visited[i][j] = True
                # Search and expand from this point.
                censor_area = deque([[i, j]])
                censor_blocks += 1
                while len(censor_area) > 0:
                    center = censor_area.popleft()
                    a, b = center[0], center[1]
                    # UPPER LINE
                    if a - 1 >= 0 and b - 1 >= 0 and (not visited[a - 1][b - 1]):
                        if area[a - 1][b - 1] == "#":
                            censor_area.append([a - 1, b - 1])
                        visited[a - 1][b - 1] = True
                    if a - 1 >= 0 and (not visited[a - 1][b]):
                        if area[a - 1][b] == "#":
                            censor_area.append([a - 1, b])
                        visited[a - 1][b] = True
                    if a - 1 >= 0 and b + 1 <= W - 1 and (not visited[a - 1][b + 1]):
                        if area[a - 1][b + 1] == "#":
                            censor_area.append([a - 1, b + 1])
                        visited[a - 1][ b + 1] = True

                    # CENTER LINE
                    if b - 1 >= 0 and (not visited[a][b - 1]):
                        if area[a][b -1] == "#":
                            censor_area.append([a, b - 1])
                        visited[a][b - 1] = True
                    # *CENTER*
                    if b + 1 <= W - 1 and (not visited[a][b + 1]):
                        if area[a][b + 1] == "#":
                            censor_area.append([a, b + 1])
                        visited[a][b + 1] = True

                    # LOWER LINE
                    if a + 1 <= H - 1 and b - 1 >= 0 and (not visited[a + 1][b - 1]):
                        if area[a + 1][b - 1] == "#":
                            censor_area.append([a + 1, b - 1])
                        visited[a + 1][b - 1] = True
                    if a + 1 <= H - 1 and (not visited[a + 1][b]):
                        if area[a + 1][b] == "#":
                            censor_area.append([a + 1, b])
                        visited[a + 1][b] = True
                    if a + 1 <= H - 1 and b + 1 <= W - 1 and (not visited[a + 1][b + 1]):
                        if area[a + 1][b + 1] == "#":
                            censor_area.append([a + 1, b + 1])
                        visited[a + 1][b + 1] = True

                # print("--broke while loop--")
                # for x in range(H):
                     # print(visited[i])
                #     for y in visited[x]:
                #         if y == True:
                #             print("T", end="")
                #         else:
                #             print("F", end="")
                #     print("")
                # print("")
                    
            else:
                visited[i][j] = True

print(censor_blocks)
