#!/usr/bin/env python3

T = int(input())

def get_intersection(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    y_or_n = (r1 - r2) ** 2 <= d <= (r1 + r2) ** 2
    if y_or_n:
        print("Yes")
    else:
        print("No")

for i in range(T):
    X1, Y1, R1, X2, Y2, R2  = map(int, input().split())

    get_intersection(X1, Y1, R1, X2, Y2, R2)
