#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

used = [False] * (N + 1)
for i in range(1, N + 1):
    cnt = A.count(i)
    if cnt >= 1:
        used[i] = True
        if cnt >= 2:
            print("No")
            exit()

unused = []
for i in range(1, N + 1):
    if not used[i]:
        unused.append(i)

used.pop(0)

print("Yes")
res = []
for i in range(N):
    if A[i] == -1:
        res.append(unused.pop(0))
    else:
        res.append(A[i])

print(*res)
