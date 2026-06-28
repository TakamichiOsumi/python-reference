#!/usr/bin/env python3

H, W = map(int, input().split())

area = []
for i in range(H):
    l = list(input())
    area.append(l)

idx = 0
while True:
    t_or_f = [ area[idx][j] == '.' for j in range(W) ]
    if all(t_or_f):
        area.pop(0)
    else:
        break
# print("done=", area)
while True:
    t_or_f = [ area[len(area) - 1][j] == '.' for j in range(W) ]
    # print(area)
    if all(t_or_f):
        area.pop(len(area) - 1)
    else:
        break

dellist = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]
columns = list(zip(*area))

idx = 0
while True:
    t_or_f = [ columns[idx][j] == '.' for j in range(len(columns[0])) ]
    if all(t_or_f):
        columns.pop(0)
    else:
        break

# print(columns)
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
