#!/usr/bin/env python3

# Key Takeaways:
#
# (1) The entire area is not large enough to scan all of maximum costs
#     from every cell.
# (2) Do not forget the initial flag set for the starting cell,
#     as described in [1].

from collections import deque

H, W = map(int, input().split())
area = [ list(input()) for _ in range(H) ]

def BFS(area, max_h, max_w, start_h, start_w):

    d = deque([(start_h, start_w, 0)])
    visited = [ [False] * max_w for _ in range(max_h) ]
    visited[start_h][start_w] = True # ... [1]

    cur_max_c = 0
    while len(d) > 0:
        cur_h, cur_w, cur_c = d.popleft()
        if cur_max_c < cur_c:
            cur_max_c = cur_c

        for m in [[-1, 0], [1, 0],
                  [0, -1], [0, 1]]:
            moved_w = cur_w + m[1]
            moved_h = cur_h + m[0]
            if (0 <= moved_w <= max_w - 1) and (0 <= moved_h <= max_h - 1) \
               and (area[moved_h][moved_w] == '.') \
               and (visited[moved_h][moved_w] is False):
                visited[moved_h][moved_w] = True
                d.append((moved_h, moved_w, cur_c + 1))

    return cur_max_c

global_max_c = 0
for i in range(H):
    for j in range(W):
        if area[i][j] == '.':
            global_max_c = max(global_max_c,
                               BFS(area, H, W, i, j))

print(global_max_c)
