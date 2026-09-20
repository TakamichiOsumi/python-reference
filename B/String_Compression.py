#!/usr/bin/env python3

import itertools

pairs = [ (k, list(g)) for k, g in itertools.groupby(list(input())) ]
# print(pairs)

char_freqs = [ (t[0], len(t[1])) for t in pairs ]
# print(char_freqs)

ans = ""
for t in char_freqs:
    c, freq = t
    ans += (c + str(freq))
print(ans)
