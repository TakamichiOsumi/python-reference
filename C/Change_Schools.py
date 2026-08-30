#!/usr/bin/env python3

from sortedcontainers import SortedDict # keys(), values(), items(), bisect_left(), bisect_right(), etc
from sortedcontainers import SortedList # add(), bisect_left(), bisect_right(), count(), extend(), index(), insert(index, value), etc
from collections import Counter # c = Counter('abcdeabc') # print(''.join(sorted(c.elements()))) => 'aabbccde'

K, N = map(int, input().split())
A = SortedDict(Counter(list(map(int, input().split()))))

class_num = [0] * K
max_num = 0
for a in A:
    class_num[a - 1] += A[a]
    max_num = max(max_num, A[a])

if N == 1:
    print(1)
else:
    added = 0
    for a in A:
        if (A[a] == (max_num - 1)) or (A[a] == max_num):
            added += 1
    print(added)
