#!/usr/bin/env python3

# Key Takeaways:
#
# 1. Learn the operand precedence to reduce typing and increase readability.
#
# The top has the highest precedencce in the below table.
# -----------------------
#     ()
#     x[index]
#     *, /, //, %
#     +, -
#     in, <, <=, >, >=, ==
#     not x
#     and
#     or
# -----------------------
#
# 2. Avoid an indent for long block logic if possible.
#    This applies to the last sum calculation logic.
#
# 3. Reuse the main logic of this problem to other breadth-first search
#    problems. Using functions such as array_idx() and matrix_idx() would
#    reduce other similar ones.

from queue import Queue

H, W = map(int, input().split())

area = [ list(input()) for _ in range(H) ]
costs = [-1] * (H * W)
costs[0] = 0

q = Queue()
q.put([0, 0])

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# Convert matrix index to array index.
def array_idx(x, y, width):
    return y * width + x

# Convert array index to matrix index.
def matrix_idx(p, width):
    x = p % width
    y = p // width
    return [x, y]

# Debug.
def show_costs_on_map(costs):
    print("")
    for start in range(0, H * W, W):
        ary = costs[start : start + W]
        ary = map(str, ary)
        ary = [ s.zfill(3) for s in ary ]
        print(*ary)

# Main
while not q.empty():
    cur_x, cur_y = q.get()
    cur_cost = costs[array_idx(cur_x, cur_y, W)]

    for m in moves:
        moved_x = cur_x + m[0]
        moved_y = cur_y + m[1]
        if 0 <= moved_x <= W - 1 and 0 <= moved_y <= H - 1:
            if costs[array_idx(moved_x, moved_y, W)] == -1 and area[moved_y][moved_x] == '.':
                q.put([moved_x, moved_y])
                costs[array_idx(moved_x, moved_y, W)] = cur_cost + 1

    # show_costs_on_map(costs)

dest_cost = costs[array_idx(W - 1, H - 1, W)]
if dest_cost == -1:
    print(-1)
    exit()

# Count the sum of (a), (b) and (c).
#
# (a) Cells that can be visited but can be excluded as
#     duplicate count routes when the shortest path is chosen.
# (b) Cells that can be never visited (surrounded by walls).
# (c) Cells that are farther than the destination cell x=W-1, y=H-1.

# (a)
duplicates = 0
for i in range(0, dest_cost + 1):
    hit_counts = costs.count(i)
    if hit_counts >= 2:
        duplicates += (hit_counts - 1)
    else:
        # No duplicate like x=0, y=0 and x=W-1, y=H-1.
        pass

# (b)
farther_cells = len(list(filter(lambda a:a > dest_cost, costs)))

# (c)
non_visited = [ i for i, x in enumerate(costs) if x == -1 ]
non_visitable = 0
for i in range(len(non_visited)):
    x, y = matrix_idx(non_visited[i], W)
    if area[y][x] == ".":
        non_visitable +=1

# The sum of (a), (b) and (c).
print(duplicates + non_visitable + farther_cells)
