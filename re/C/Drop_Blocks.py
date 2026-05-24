#!/usr/bin/env python3

# This code was evaluated as TLE.

N, Q = map(int, input().split())

N_cell_position = {}
for i in range(N):
    N_cell_position[i] = 0

block_nums_cells = { }
block_nums_cells[0] = set(range(N))

base = 0

for i in range(Q):
    no, x_y = map(int, input().split())
    if no == 1:
        x_y = x_y - 1
        added_cell = x_y

        cur_block_key = N_cell_position[added_cell]
        block_nums_cells[cur_block_key].remove(added_cell)
        if (cur_block_key + 1) not in block_nums_cells.keys():
            block_nums_cells[cur_block_key + 1] = set([])
        block_nums_cells[cur_block_key + 1].add(added_cell)
        N_cell_position[added_cell] = cur_block_key + 1
        if len(block_nums_cells[0]) == 0:
            for i in range(1, len(block_nums_cells.keys())):
                tmp = block_nums_cells[i]
                block_nums_cells[i - 1] = None
                block_nums_cells[i - 1] = tmp
            for k in N_cell_position.keys():
                N_cell_position[k] -= 1

            block_nums_cells[len(block_nums_cells.keys()) - 1] = set()

    elif no == 2:

        total = 0
        for k in block_nums_cells.keys():
            if k >= x_y:
                total += len(block_nums_cells[k])
        print(total)

