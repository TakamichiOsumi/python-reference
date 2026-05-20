#!/usr/bin/env python3

N, K = map(int, input().split())

cur_sum = K

div = 10 ** 9

ary = [1] * K
for i in range(K, N + 1):
    ary.append(cur_sum)

    cur_sum -= ary[i - K];
    cur_sum += ary[i]

    cur_sum %= div

print(ary[N])

