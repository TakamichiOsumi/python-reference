#!/usr/bin/env python3

import re

S = input()

splited = []
# Split the entire string when it encounters a different character.
for m in re.finditer(r"1+|2+|3+|4+|5+|6+|7+|8+|9+|0+", S):
    splited.append(S[ m.start(0) : m.end(0) ])

ans = 0
for i in range(len(splited) - 1):
    if int(splited[i][0]) + 1 == int(splited[i + 1][0]):
        ans += min(len(splited[i]),
                   len(splited[i + 1]))

print(ans)
