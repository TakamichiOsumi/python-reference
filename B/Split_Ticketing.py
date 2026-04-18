#!/usr/bin/env python3

import itertools

N = int(input())

costs = [ list(map(int, input().split())) for _ in range(N - 1) ]

def found_cheap_route(start, transit, end, cost_mat):
    c1 = cost_mat[start][end]
    c2 = cost_mat[start][transit] + cost_mat[transit][end]
    if c1 > c2:
        return True
    else:
        return False

perms = itertools.permutations(range(0, N), 3)
padding = 1
cost_mat = []
for i in range(len(costs)):
    l = costs[i]
    for j in range(padding):
        l.insert(0, 0)
    padding +=1
    cost_mat.append(l)

exist = False
for p in perms:
    p = list(p)
    start = min(p)
    end = max(p)
    p.pop(p.index(end))
    p.pop(p.index(start))
    if found_cheap_route(start, p[0], end, cost_mat):
        exist = True
        break

if exist:
    print("Yes")
else:
    print("No")
