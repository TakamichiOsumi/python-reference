#!/usr/bin/env python3

# import pdb

N = int(input())
X, A, B = map(int, input().split())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
    # pdb.set_trace()

if True:
    print("Yes") # "YES"
else:
    print("No") # "NO"
