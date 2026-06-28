#!/usr/bin/env python3

N, M = map(int, input().split())

my_ary = [0] * N

date_and_colors = []
for _ in range(M):
    date_and_colors.append([])

for i in range(N):
    A, D, B = map(int, input().split())
    if A == B:
        my_ary[B - 1] += 1
        continue

    if D == 1:
        my_ary[B - 1] += 1
    else:
        # Append -1 & +1
        my_ary[A - 1] += 1
        date_and_colors[D - 1].append([A - 1, B - 1])

count = 0
for i in range(N):
    if my_ary[i] >= 1:
        count += 1

for d_and_c in date_and_colors:
    if len(d_and_c) == 0:
        pass
    else:
        for i in range(len(d_and_c)):
            removed, added = d_and_c[i][0], d_and_c[i][1]
            my_ary[removed] -= 1
            if my_ary[removed] == 0:
                count -= 1
            if my_ary[added] == 0:
                count += 1
            my_ary[added] += 1

    print(count)
