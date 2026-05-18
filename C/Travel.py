#!/usr/bin/env python3

import itertools

N, K = map(int, input().split())

Times = []
for i in range(N):
    T = list(map(int, input().split()))
    Times.append(T)

routes = list(itertools.permutations(list(range(1, N))))
same_cost_count = 0
for route in routes:
    route = list(route)
    route.insert(0, 0)
    route.insert(len(route), 0)

    cost = 0
    for i in range(len(route) - 1):
        orig = route[i]
        dest = route[i + 1]
        cost += Times[orig][dest]
    if cost == K:
        same_cost_count += 1

print(same_cost_count)
