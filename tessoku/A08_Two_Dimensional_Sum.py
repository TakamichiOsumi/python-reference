#!/usr/bin/env python3

debug = False # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

H, W = map(int, input().split())
area = [ list(map(int, input().split())) for _ in range(H) ]
Q = int(input())
ABCD = [ list(map(int, input().split())) for _ in range(Q) ]

p("area=", area)
p("ABCD=", ABCD)

vert = [[0] * W for _ in range(H) ]

for i in range(H):
    total = 0
    for j in range(W):
        total += area[i][j]
        vert[i][j] = total

p("*vert*")
for i in range(H):
    p(vert[i])

for abcd in ABCD:
    a, b, c, d = abcd
    a, b, c, d = a - 1, b - 1, c - 1, d - 1
    p("a,b,c,d:", a, b, "=>", c, d)
    total = 0
    for i in range(a, c + 1):
        # If the left edge index starts from the 0,
        # which means b == 0, there's no need to calculate
        # the diff for vert[i][b - 1].
        # Since the selection range starts at the leftmost
        # cell, there are no values to substract.
        if b == 0:
            minus = 0
        else:
            # Sum value for each row can be calculated by the
            # reference of cumulative sum. Required range to
            # sum start from b to d. So, sum values until index
            # [b - 1] should be removed.
            minus = vert[i][b - 1]
        total += (vert[i][d] - minus)
    print(total)
