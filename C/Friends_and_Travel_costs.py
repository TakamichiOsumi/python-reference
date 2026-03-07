#!/usr/bin/env python3

import sortedcontainers

N, K = map(int, input().split())

position_and_coin = {}
for i in range(N):
    A, B = map(int, input().split())
    if A in position_and_coin.keys():
        position_and_coin[A] = position_and_coin[A] + B
    else:
        position_and_coin[A] = B

dest = K
positions = sortedcontainers.SortedList((position_and_coin.keys()))

while True:

    encounter = list(positions.irange(0, dest))

    if len(encounter) == 0:
        break
    else:
        total = 0
        for i in range(len(encounter)):
            total += position_and_coin[encounter[i]]
            positions.discard(encounter[i])
        dest += total

print(dest)

