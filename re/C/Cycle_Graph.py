#!/usr/bin/env python3

from collections import deque

# Key Takeaways:
#
# Regard 'Cycle Graph' as a graph that satisfies two points.
# a - Each edge as two connections.
# b - All edge can be visited.

N, M = map(int, input().split())
edgeIdx_connections = [ [] for _ in range(N) ]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edgeIdx_connections[a].append(b)
    edgeIdx_connections[b].append(a)

visited = [False] * N

# Set the initial position.
visited[0] = [True]
que = deque([0])

while que:
    edgeIdx = que.popleft()
    for conn in edgeIdx_connections[edgeIdx]:
        if not visited[conn]:
            visited[conn] = True
            que.append(conn)

if not all(visited):
    print("No")
else:
    if all(len(conns) == 2 for conns in edgeIdx_connections):
        print("Yes")
    else:
        print("No")
