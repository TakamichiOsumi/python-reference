#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Iterate a list item by the syntax 'for item in items:'
#
# (2) Get used to the logics to calculate 'point symmetry'
#     in a specific range within matrix.
#
#     Suppose the four corners of the range is decided by
#     min(height_range)    = top left
#     max(height_range)    = bottom left
#     min(width_range)     = top left
#     and max(width_range) = top right.
#
#     If the base cell is area[height][width], then
#     the target cell to compare can be calculated as below.
#    -------------------------------------------------------------
#     comp_height = min(height_range) + max(height_range) - height
#     comp_width = min(width_range) + max(width_range) - width
#     area[height][width] == area[comp_height][comp_width]
#    -------------------------------------------------------------

import itertools

H, W = map(int, input().split())

def is_point_symmetry(h, w, area):
    # Convert range two numbers to full numbers list to iterate.
    #
    # The last '+ 1' is a number to make single row/column
    # iterable.
    h_set = set(range(h[0], h[1] + 1))
    w_set = set(range(w[0], w[1] + 1))
    for i in h_set:
        for j in w_set:
            h_idx = h[0] + h[1] - i
            w_idx = w[0] + w[1] - j
            if area[i][j] != area[h_idx][w_idx]:
                return False

    return True

# The idea of implementation.
#
# At first, decide the scope to scan the point symmetry.
# This requires the itertools.combinations to pick up the
# all of the combinations of indexes for height and width.
#
# Secondly, convert the range decided by two numbers
# to the full indexes list. The full list becomes the
# indexes to iterate the cell one by one, when
# both one for the width and the other for the height
# are used. See the detail in is_point_symmetry().
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
