#!/usr/bin/env python3

from queue import Queue

H, W = map(int, input().split())

area = [ list(input()) for _ in range(H) ]
dist = [-1] * (H * W)
dist[0] = 0

q = Queue()
q.put([0, 0])

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# Convert matrix index to array index.
def dist_idx(x, y, width):
    return y * width + x

# Convert array index to matrix index.
def area_idx(p, width):
    x = p % width
    y = p // width
    return [x, y]

# Debug.
def show_dist_as_map(dist):
    print("")
    for start in range(0, H * W, W):
        ary = dist[start : start + W]
        ary = map(str, ary)
        ary = [ s.zfill(3) for s in ary ]
        print(*ary)

while not q.empty():
    cur_x, cur_y = q.get()
    cur_cost = dist[dist_idx(cur_x, cur_y, W)]

    for m in moves:
        new_x = cur_x + m[0]
        new_y = cur_y + m[1]
        if (0 <= new_x <= (W - 1)) and (0 <= new_y <= (H - 1)):
            if (dist[dist_idx(new_x, new_y, W)] == -1) and (area[new_y][new_x] == '.'):
                q.put([new_x, new_y])
                dist[dist_idx(new_x, new_y, W)] = cur_cost + 1
    # show_dist_as_map(dist)

dest_cost = dist[dist_idx(W - 1, H - 1, W)]
if dest_cost == -1:
    print(-1)
else:
    # Count the sum of (a), (b) and (c).
    #
    # (a) Cells that can be visited but can be excluded as
    #     duplicate count routes when the shortest path is chosen.
    # (b) Cells that can be never visited (surrounded by walls).
    # (c) Cells that are farther than the destination cell x=W-1, y=H-1.

    # (a)
    duplicates = 0
    for i in range(0, dest_cost + 1):
        hit_counts = dist.count(i)
        if hit_counts >= 2:
            duplicates += (hit_counts - 1)
        else:
            # No duplicate like x=0, y=0 and x=W-1, y=H-1.
            pass

    # (b)
    farther_cells = len(list(filter(lambda a:a > dest_cost, dist)))

    # (c)
    non_visited = [ i for i, x in enumerate(dist) if x == -1 ]
    non_visitable = 0
    for i in range(len(non_visited)):
        x, y = area_idx(non_visited[i], W)
        if area[y][x] == ".":
            non_visitable +=1
    print(duplicates + non_visitable + farther_cells)
