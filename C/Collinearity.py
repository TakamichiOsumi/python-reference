#!/usr/bin/env python3

import itertools
from fractions import Fraction

N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

def successful_exit():
    print("Yes")
    exit()
    
for verified_points in itertools.combinations(points, 3):
    p1, p2, p3 = verified_points

    if p1[0] - p2[0] != 0:
        a = Fraction((p1[1] - p2[1]), (p1[0] - p2[0]))
        if a != 0:
            # y = ax + b
            b = p1[1] - (a * p1[0])
            if p3[1] == a * p3[0] + b:
                successful_exit()
        else:
            # y = b
            if p3[1] == p1[1]:
                successful_exit()
    else:
        # x = a
        if p3[0] == p1[0]:
            successful_exit()

print("No")
