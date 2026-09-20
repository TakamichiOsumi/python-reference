#!/usr/bin/env python3

from atcoder.segtree import SegTree

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

def max_op(data1, data2):
    if data1[0] > data2[0]:
        return data1
    else:
        return data2

def min_op(data1, data2):
    if data1[0] < data2[0]:
        return data1
    else:
        return data2

N, M = map(int, input().split())
P = list(map(int, input().split()))
ex_P = [ [val, idx] for idx, val in enumerate(P) ]

p(P)
p(ex_P)

min_seg = SegTree(min_op, [10 ** 9,    -1], ex_P)
max_seg = SegTree(max_op, [-(10 ** 9), -1], ex_P)

for i in range(M):
    l, r = map(int, input().split())
    l -= 1
    min_val, min_idx = min_seg.prod(l, r)
    max_val, max_idx = max_seg.prod(l, r)

    tmp = ex_P[max_idx]
    ex_P[max_idx] = ex_P[min_idx]
    ex_P[min_idx] = tmp
    p("swap: ", min_idx, "<=>", max_idx)

    min_seg.set(min_idx, [max_val, min_idx])
    min_seg.set(max_idx, [min_val, max_idx])

    max_seg.set(min_idx, [max_val, min_idx])
    max_seg.set(max_idx, [min_val, max_idx])

    p("updated ex_P=", ex_P)

ans = [val[0] for idx, val in enumerate(ex_P)]
print(*ans)
