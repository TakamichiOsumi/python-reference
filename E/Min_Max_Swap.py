#!/usr/bin/env python3

# from sortedcontainers import SortedDict # keys(), values(), items(), bisect_left(), bisect_right(), etc
# from sortedcontainers import SortedList # add(), bisect_left(), bisect_right(), count(), extend(), index(), insert(index, value), etc
# from sortedcontainers import SortedSet # add(), remove(), etc
# from collections import deque # append(), appendleft(), extend(), extendleft(), index(), pop(), popleft(), etc
# from collections Counter # c = Counter('abcdeabc') # print(''.join(sorted(c.elements()))) => 'aabbccde'
# import itertools # itertools.permutations(range(A, B)), itertools.combinations(range(A, B), C),
#                  # itertools.product(range(A, B), range(C, D)), etc
# import numpy
# import re # for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):

from atcoder.segtree import SegTree

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

#print(P)
#print(ex_P)

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
#    print("swap: ", min_idx, "<=>", max_idx)

    min_seg.set(min_idx, [max_val, min_idx])
    min_seg.set(max_idx, [min_val, max_idx])

    max_seg.set(min_idx, [max_val, min_idx])
    max_seg.set(max_idx, [min_val, max_idx])

#    print("updated ex_P=", ex_P)

# print(*ex_P)
ans = [val[0] for idx, val in enumerate(ex_P)]
print(*ans)
