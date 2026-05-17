#!/usr/bin/env python3

# import pdb

# from sortedcontainers import SortedList
# from collections import deque
# import itertools
# import numpy
import re

S = input()

count = 0

for m in re.finditer(r"C", S):
    # print("Index=", m.start(0), "&", m.end(0), ", Sub string : ", S[ m.start(0) : m.end(0) ])

    center_C = m.start(0)
    close_edge = min(center_C, (len(S) - 1) - center_C)
    count += (close_edge + 1)
    # print("close_edge=", close_edge)

print(count)
