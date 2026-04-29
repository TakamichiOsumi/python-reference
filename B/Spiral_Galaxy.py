#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Get used to the logics to calculate 'point symmetry'
#     in a specific range of matrix.
#
#     comp_height = min(height_range) + max(height_range) - height
#     comp_width = min(width_range) + max(width_range) - width
#     area[height][width] == area[comp_height][comp_width]
#
# (2) Iterate a list item by the syntax 'for item in items:'

import itertools

H, W = map(int, input().split())

def is_point_symmetry(h, w, area):
    # Convert range two numbers to numbers list to iterate.
    h_set = set(range(h[0], h[1] + 1))
    w_set = set(range(w[0], w[1] + 1))
    for i in h_set:
        for j in w_set:
            h_idx = h[0] + h[1] - i
            w_idx = w[0] + w[1] - j
            if area[i][j] != area[h_idx][w_idx]:
                return False

    return True

h_ary = list(itertools.combinations(range(0, H), 2))
w_ary = list(itertools.combinations(range(0, W), 2))

h_ary.extend([(i, i) for i in range(H)])
w_ary.extend([(i, i) for i in range(W)])

S = [input() for _ in range(H)]

count = 0
for h in h_ary:
    for w in w_ary:
        if is_point_symmetry(list(h), list(w), S):
            count += 1

print(count)
