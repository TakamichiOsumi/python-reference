#!/usr/bin/env python3

import itertools

X = list(input())

X_len = len(X)

perms = list(itertools.permutations(X))

min_val = 10 ** 6
for perm in perms:
    s = ''.join(list(perm))
    if len(str(int(s))) == X_len:
        min_val = min(min_val, int(s))

print(min_val)


