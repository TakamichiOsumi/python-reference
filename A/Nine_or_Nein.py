#!/usr/bin/env python3

# from sortedcontainers import SortedList, SortedDict, SortedSet
# from collections import deque, Counter
# import itertools
# import numpy
# import re

A, B = map(int, input().split())


if A + B == 9 or A - B == 9 or A * B == 9 or A / B == 9:
    print("Nine")
else:
    print("Nein")
