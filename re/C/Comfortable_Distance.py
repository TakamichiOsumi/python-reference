#!/usr/bin/env python3

N, L, R = map(int, input().split())

S = input()

count = 0

for i in range(N):
    for j in range(R - L + 1):
        if i + j + L > N - 1:
            break
        if S[i] == S[i + j + L]:
            count += 1

print(count)
