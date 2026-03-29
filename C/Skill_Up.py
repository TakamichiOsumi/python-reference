#!/usr/bin/env python3

import itertools

N, M, X = map(int, input().split())

new_knowledges = []
cur_state = []

for i in range(N):
    C_A = list(map(int, input().split()))
    new_knowledges.append(C_A)

lowest_price = 10 ** 15
for i in range(2 ** N):
    bag = []
    for j in range(N):
        if ((i >> j) & 1):
            bag.append(new_knowledges[j])
    total = [0] * M
    for book in bag:
        total = [x + y for x, y in zip(total, book[1:])]

    if sum([True for x in total if x >= X ]) >= M:
        cur_price = 0
        for book in bag:
            cur_price += book[0]
        lowest_price = min(lowest_price, cur_price)

if lowest_price == 10 ** 15:
    print(-1)
else:
    print(lowest_price)
