#!/usr/bin/env python3

S = list(input())

chars = set(S)

freq_dict = {}
for c in chars:
    freq_dict[c] = S.count(c)

counts = freq_dict.values()
max_val = max(counts)

removed_chars = []
for char, count in freq_dict.items():
    if max_val == count:
        removed_chars.append(char)

print("".join([c for c in S if not c in removed_chars]))
