#!/usr/bin/env python3

N, M, Q = map(int, input().split())

edges = []
for i in range(M):
    # The input index of vertex starts from 1 and N.
    start_edge, end_edge = map(int, input().split())
    edges.append([start_edge, end_edge])

# The index of vertex_colors is 0 ... N - 1.
vertex_colors = list(map(int, input().split()))
for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        print(vertex_colors[query[1] - 1])
        for j in range(M):
            start_edge, end_edge = edges[j]
            if start_edge == query[1]:
                vertex_colors[end_edge - 1] = vertex_colors[start_edge - 1]
            elif end_edge == query[1]:
                vertex_colors[start_edge - 1] = vertex_colors[end_edge - 1]
            else:
                pass
    else:
        print(vertex_colors[query[1] - 1])
        vertex_colors[query[1] - 1] = query[2]
