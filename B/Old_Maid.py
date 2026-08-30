#!/usr/bin/env python3

# from sortedcontainers import SortedDict # keys(), values(), items(), bisect_left(), bisect_right(), etc
# from sortedcontainers import SortedList # add(), bisect_left(), bisect_right(), count(), extend(), index(), insert(index, value), etc
# from sortedcontainers import SortedSet # add(), remove(), etc
# from collections import deque # append(), appendleft(), extend(), extendleft(), index(), pop(), popleft(), etc
from collections import Counter # c = Counter('abcdeabc') # print(''.join(sorted(c.elements()))) => 'aabbccde'
# import itertools # itertools.permutations(range(A, B)), itertools.combinations(range(A, B), C),
#                  # itertools.product(range(A, B), range(C, D)), etc
# import numpy
# import re # for m in re.finditer(r"(aa+)|(bb+)|(cc+)", s):

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
B = list(map(int, input().split()))
c = Counter(B)
# print(c)

ans = 0
for k in c.keys():
    if c[k] >= 2:
        no = (c[k] % 2)
        ans += (k * no)
    elif c[k] == 1:
        ans += k

print(ans)
