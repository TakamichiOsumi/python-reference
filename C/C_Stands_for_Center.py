#!/usr/bin/env python3

import re

S = input()

count = 0

for m in re.finditer(r"C", S):
    center_C = m.start(0)
    close_edge = min(center_C, (len(S) - 1) - center_C)
    count += (close_edge + 1)

print(count)
