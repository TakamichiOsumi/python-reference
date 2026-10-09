#!/usr/bin/env python3

# Key Takeaways:
#
# Name long distictive variable names such as 'item_idx' and 'cur_weight',
# rather than short names like 'i' and 'j' for DP problems.
#
# This will allow easier understanding and faster problem solving.

debug = True # switch
def p(*var):
    global debug
    if debug:
        if len(var) and type(var[0]) == type([]):
            print("DEBUG : dump array:")
            for i in range(len(var[0])):
                print("\t", end = "")
                print(i, var[0][i])
        else:
            print("DEBUG:", *var)

N, W = map(int, input().split())
w_v = [ list(map(int, input().split())) for _ in range(N) ]
# Insert a single dummy data to skip 0th item at [1] row.
w_v.insert(0, [0, 0])
p(w_v)

value_matrix = [ [0] * (W + 1) for _ in range(N + 1) ]

for item_idx in range(1, N + 1): # ... [1]
    item_weight, item_value = w_v[item_idx][0], w_v[item_idx][1]

    for cur_weight in range(W + 1):
        if cur_weight == item_weight:
            value_matrix[item_idx][cur_weight] = item_value
        if item_idx - 1 >= 0:
            # At least, single upper row exists.
            if value_matrix[item_idx - 1][cur_weight] != 0:
                # Inherit the value of the upper row.
                value_matrix[item_idx][cur_weight] = value_matrix[item_idx - 1][cur_weight]

            # If 'cur_weight' (the current item's weight) - 'item_weight' is equal or bigger than zero,
            # there might be values in some existing upper cells in the 'value_matrix'.
            #
            # Update any value if a new value is bigger than the current written value in the cell.
            if cur_weight - item_weight >= 0 and value_matrix[item_idx - 1][cur_weight - item_weight] != 0:
                possible_value = value_matrix[item_idx - 1][cur_weight - item_weight] + item_value
                value_matrix[item_idx][cur_weight] = max(value_matrix[item_idx][cur_weight], possible_value)
    p(value_matrix)

print(max(value_matrix[N]))
