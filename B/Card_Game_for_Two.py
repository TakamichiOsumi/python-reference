#!/usr/bin/env python3

N = int(input())
ary = list(map(int, input().split()))

ary.sort(reverse = True)

turn = 0
Alice = 0
Bob = 0

while len(ary) > 0:
    if turn % 2 == 0:
        Alice = Alice + ary.pop(0)
    if turn % 2 == 1:
        Bob = Bob + ary.pop(0)
    turn = turn + 1

print(Alice - Bob)
