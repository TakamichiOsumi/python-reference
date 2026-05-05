#!/usr/bin/env python3

import numpy
import itertools

H, W, K = map(int, input().split())

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

patterns = 0
for row_column_pair in itertools.product(H_patterns, W_patterns):
    removed_blacks = count_black_cells(row_column_pair, area)
    if black_cells - removed_blacks == K:
        patterns += 1

print(patterns)
