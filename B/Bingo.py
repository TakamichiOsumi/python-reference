#!/usr/bin/env python3

marked = [[False] * 3, [False] * 3, [False] * 3]
my_card = []
for i in range(3):
    row = list(map(int, input().split()))
    my_card.append(row)

N = int(input())
for n in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if my_card[i][j] == b:
                marked[i][j] = True

bingo = False
for i in range(3):
    if sum(marked[i]) == 3:
        bingo = True
for i in range(3):
    if sum([marked[0][i], marked[1][i], marked[2][i]]) == 3:
        bingo = True
if sum([marked[0][0], marked[1][1], marked[2][2]]) == 3:
    bingo = True
if sum([marked[0][2], marked[1][1], marked[2][0]]) == 3:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
