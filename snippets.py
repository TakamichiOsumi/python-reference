#!/usr/bin/env python3

# import pdb

# N = int(input())
N, M = map(int, input().split())
X, A, B = map(int, input().split())

count = 0

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])
    # pdb.set_trace()

print(count)
if True:
    print("Yes") # "YES"
else:
    print("No") # "NO"
