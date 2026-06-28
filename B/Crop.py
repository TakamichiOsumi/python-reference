#!/usr/bin/env python3

H, W = map(int, input().split())

area = [ list(input()) for _ in range(H) ]

while True:
    t_or_f = [ area[0][j] == '.' for j in range(W) ]
    if all(t_or_f):
        area.pop(0)
    else:
        break

while True:
    t_or_f = [ area[len(area) - 1][j] == '.' for j in range(W) ]
    if all(t_or_f):
        area.pop(len(area) - 1)
    else:
        break

columns = list(zip(*area))

while True:
    t_or_f = [ columns[0][j] == '.' for j in range(len(columns[0])) ]
    if all(t_or_f):
        columns.pop(0)
    else:
        break

while True:
    t_or_f = [ columns[len(columns) - 1][j] == '.' for j in range(len(columns[0])) ]
    if all(t_or_f):
        columns.pop(len(columns) - 1)
    else:
        break

rows = list(zip(*columns))
for r in rows:
    r = list(r)
    print("".join(r))
