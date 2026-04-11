#!/usr/bin/env python3

x, y = map(int, input().split())

if x != y:
    ary = [0, 1, 2]
    ary.remove(x)
    ary.remove(y)
    print(ary[0])
else:
    print(x)

