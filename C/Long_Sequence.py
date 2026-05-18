#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Treat the problem input either as index of array or as original number
#     in a consistent manner. In this problem, K is the former. In the entire
#     code, unify the usage, to avoid the confusion.

N, K = map(int, input().split())

K -= 1

database = []
for i in range(N):
    L, *A = list(map(int, input().split()))
    database.append(A)

C = list(map(int, input().split()))

prev_index = cur_index = 0
for i in range(N):
    prev_index = cur_index
    cur_index += (len(database[i]) * C[i])
    if cur_index > K:
        idx = (K - prev_index) % len(database[i])
        print(database[i][idx])
        break
