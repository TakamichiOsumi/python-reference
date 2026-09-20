#!/usr/bin/env python3

N = int(input())
S = input()
T = input()

possible = True
for i in range(N):
    if T[i] == '*':
        continue
    if S[i] == T[i]:
        pass
    else:
        print("No")
        exit()
print("Yes")
