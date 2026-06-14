#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Estimate the maximum memory size of the solution.
#     This will reduce the time loss for runtime error
#     caused by RE(MLE).
# (2) Avoid add() to add each list member to SortedSet.
#     Use update().

from sortedcontainers import SortedSet

N, M = map(int, input().split())

points = SortedSet([])

for i in range(M):
    R, C = map(int, input().split())
    R, C = R - 1, C - 1

    point = R * N + C
    if (R + 1) <= (N - 1) and (C + 1) <= (N - 1):
        area = SortedSet([point,
                          point + 1,
                          point + N,
                          point + N + 1])
        if len(points & area) >= 1 :
            continue
        else:
            points.update([point, point + 1, point + N, point + N + 1])

print(len(points) // 4)
