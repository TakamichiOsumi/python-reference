#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
# Make the logic simple by adding 0 at the beginning.
A.insert(0, 0)

consume = cur_right_edge = 1

for i in range(1, N):
    if i + A[i] - 1 > cur_right_edge:
        cur_right_edge = min(i + A[i] - 1, N)
        # Restart the count from A[i] - 1.
        #
        # When the cur_right_edge gets updated,
        # 'consume' count can start from
        # replacing domino's height, which is
        # A[i] - 1.
        consume = A[i] - 1
    else:
        consume -= 1

    if consume <= 0:
        break

print(cur_right_edge)
