#!/usr/bin/env python3

import itertools

def runLengthEncode(string, get_freqs):
    chars = list(string)
    pairs = [ (k, list(g)) for k, g in itertools.groupby(chars) ]
    char_freqs = [ (t[0], len(t[1])) for t in pairs ]
    if get_freqs:
        return char_freqs
    ans = ""
    for t in char_freqs:
        c, freq = t
        ans += (c + str(freq))
    return ans

S = input()

length =len(runLengthEncode(S, True))
if length == 1:
    print("0")
else:
    print(length - 1)
