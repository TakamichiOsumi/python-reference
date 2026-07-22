#!/usr/bin/env python3

S = input()

for i, c in enumerate(list(S)):
    if S.count(c) == 1:
        print(c)
        break
