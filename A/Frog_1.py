#!/usr/bin/env python3

N = int(input())
cost_ary = list(map(int, input().split()))

buf = [0] * N
val = abs(cost_ary[0] - cost_ary[1])

if N == 2:
    print(val)
    exit()

buf[1] = val

cur_index = 2
while True:

    c1 = buf[cur_index - 1] + abs(cost_ary[cur_index - 1] - cost_ary[cur_index])
    c2 = buf[cur_index - 2] + abs(cost_ary[cur_index - 2] - cost_ary[cur_index])

    buf[cur_index] = min(c1, c2)

    if cur_index == N - 1:
        print(buf[cur_index])
        exit()

    cur_index += 1
