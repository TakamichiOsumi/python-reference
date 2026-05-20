#!/usr/bin/env python3

# Key Takeaways:
#
# (1) In this problem, applying T to numpy.array([]) was
#     slower than just computing the columns_sum array.

H, W = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(H) ]
rows_sum = [ sum(matrix[i]) for i in range(H) ]

columns_sum = []
for j in range(W):
    total = 0
    for i in range(H):
        total += matrix[i][j]
    columns_sum.append(total)

for i in range(H):
    for j in range(W):
        dup = matrix[i][j]
        val = rows_sum[i] + columns_sum[j] - dup
        print(val, end = "")
        print(" ", end="")
    print("")
