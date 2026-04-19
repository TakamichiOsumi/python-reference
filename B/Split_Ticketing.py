#!/usr/bin/env python3

import itertools

N = int(input())

# Key Takeaways:
#
# 1.  Write a simple logic to append zeros for the matrix of cost lists.
#
#     Avoid for loop and use list comprehension as described below.
#     This simplifies the entire program and doesn't define unused variables,
#     like 'padding' or 'l'.
#
#     * for loop
#
#      padding = 1
#      cost_mat = []
#      for i in range(len(costs)):
#         l = costs[i]
#         for j in range(padding):
#            l.insert(0, 0)
#         padding +=1
#         cost_mat.append(l)
#
#     * list comprehension
#
#      cost_mat = [ [0] * (i+1) + list(map(int, input().split())) for i in range(N - 1) ]
#
# 2. Indicate the concrete number to select items for itertools functions.
#
# 3. Set a valid initial value for a True/False flag variable.
#
#    If the logic is to find something, 'found' flag should be false at the beginning.

cost_mat = [ [0] * (i+1) + list(map(int, input().split())) for i in range(N - 1) ]

def found_cheap_route(start, transit, end, cost_mat):
    c1 = cost_mat[start][end]
    c2 = cost_mat[start][transit] + cost_mat[transit][end]
    if c1 > c2:
        return True
    else:
        return False

lists = map(list, itertools.permutations(range(0, N), 3))

found = False
for l in lists:
    start = min(l)
    end = max(l)
    l.pop(l.index(end))
    l.pop(l.index(start))
    transit = l[0]
    if found_cheap_route(start, transit, end, cost_mat):
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
