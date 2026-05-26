#!/usr/bin/env python3

N, M = map(int, input().split())

my_dict = {}
for i in range(1, N + 1):
    my_dict[i] = set()

for _ in range(M):
    a, b = map(int, input().split())
    my_dict[a].add(b)
    my_dict[b].add(a)

cnt = 0
for i in range(1, N + 1):
    l = list(my_dict[i])
    smaller = list(filter(lambda x:x < i, l))
    if len(smaller) == 1:
        cnt += 1
print(cnt)
