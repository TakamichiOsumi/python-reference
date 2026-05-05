#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Get used to numpy.array and numpy.array.T.
#     The numpy.array.T allows an easier access to matrix columns,
#     according to problem conditions.
# (2) Matrix transpose cannot be applied to numpy.array type
#     when row is a string and each character isn't separated as list.
# (3) For reference, add notes of numpy.array's basic operations
#     such as ndim, shape[0] and shape[1].

import numpy
import itertools

H, W, K = map(int, input().split())

# Return the 2 ** N patterns from integer N input.
def bit_brute_force_patterns(N):
    combinations = []
    for i in range(2 ** N):
        ary = []
        for j in range(N):
            if ((i >> j) & 1):
                ary.append(j)
        combinations.append(ary)

    return combinations


def count_black_cells(row_column_pair, area):
    rows, columns = row_column_pair
    count = 0

    if len(rows) == 0 and len(columns) == 0:
        return count
    elif len(rows) == 0 and len(columns) != 0:
        area_T = area.T
        for i in columns:
            count += list(area_T[i]).count('#')
        return count
    elif len(rows) != 0 and len(columns) == 0:
        for i in rows:
            count += list(area[i]).count('#')
        return count
    elif len(rows) != 0 and len(columns) != 0:
        # Count existing black cells, including duplicates.
        for i in rows:
            count += list(area[i]).count('#')
        area_T = area.T
        for i in columns:
            count += list(area_T[i]).count('#')

        # Remove the duplicates.
        duplicates = itertools.product(rows, columns)
        for cell_idx in duplicates:
            y, x = cell_idx
            if area[y][x] == '#':
                count -= 1

        return count


raw_area = [ list(input()) for _ in range(H) ]
black_cells = sum([ raw_area[i].count('#') for i in range(H) ])
area = numpy.array(raw_area)

# Bit Brute Force for each row and column.
H_patterns = bit_brute_force_patterns(H)
W_patterns = bit_brute_force_patterns(W)


# The main logic
#
# (a) Prepare a full list of bit brute force combinations for row
#     and column. Then, cover full row and column pairs by
#     itertools.product().
# (b) Process one pair of selection of row and that of column,
#     one by one.
# (c) Considering blank input cases ([]), count the black cells.
#     Utilize the numpy's T attribute to access the columns.
#     When both numbers of selection for rows and columns exceed
#     one, counting the black cells contains some overlapped cells.
#     Return the number without the duplicates.
#     See the detail in count_black_cells().
# (d) If black cells in the rows and columns pair are removed
#     and the left number of black cells are equal to K, this is
#     a new pattern to satisfy the problem.
patterns = 0
for row_column_pair in itertools.product(H_patterns, W_patterns):
    removed_blacks = count_black_cells(row_column_pair, area)
    if black_cells - removed_blacks == K:
        patterns += 1

print(patterns)
