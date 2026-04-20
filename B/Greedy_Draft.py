#!/usr/bin/env python3

N, M = map(int, input().split())

taken = [False] * (M + 1)

answers = []
for i in range(N):
    L = int(input())
    X = map(int, input().split())

    water = True
    for x in X:
        if taken[x] == False:
            taken[x] = True
            water = False
            answers.append(x)
            break

    if water:
        answers.append(0)

for ans in answers:
    print(ans)
