#!/usr/bin/env python3

# Key Takeaways:
#
# (1) list.append() is an operation of O(1).
#
# (2) The current sum can be calculated by an idea to
#     computing the sum of one specific reagion surrounded by
#     ary[i - k] ~ ary[i] when i starts from the index = K.
#     Removing ary[i - k] and adding ary[i] means shifting
#     this reagion from left to right, one by one.

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

