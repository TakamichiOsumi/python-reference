#!/usr/bin/env python3

# Key Takeaways:
#
# (1) The problem defines (y, x) as (i, j). The problem
#     description might change the intuitive order.
#     (Or, don't skip reading the details of the
#     description.)
# (2) Inserting multiple values to multiple varialbes
#     can improve the readability of the source code,
#     like 'r, c = (r - 1) % N, (c + 1) % N'.

N = int(input())

mat = [[-1] * N for _ in range(N)]

r = 0
c = (N - 1) // 2
mat[r][c] = k = 1

for i in range(N ** 2 - 1):
    tmp_r, tmp_c = (r - 1) % N, (c + 1) % N
    if mat[tmp_r][tmp_c] != -1:
        tmp_r, tmp_c = (r + 1) % N, c
    mat[tmp_r][tmp_c] = k + 1
    r, c = tmp_r, tmp_c
    k += 1

for i in range(N):
    print(*mat[i])
