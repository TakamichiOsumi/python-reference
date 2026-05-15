#!/usr/bin/env python3

import re

S = input()

sub_strings = []
prev_end = 0
for m in re.finditer(r"(aa+)|(bb+)|(cc+)", S):
    # The 'S' starts with same char sequences.
    # Skip the first same char block.
    if m.start(0) == 0:
        prev_end = m.end(0) - 1
        continue

    # m.start(0) points to the first character of
    # "aa...", "bb...", "cc...". Then, to include
    # the frist character of the same char sequences,
    # the end index needs to point the second character
    # for them. + 1 is for it.
    sub_strings.append(S[prev_end:m.start(0) + 1])

    # As for the previous end index, the explanation
    # becomes similar to the previous one. The
    # m.end(0) is the right after the same char sequences.
    # So, to include the last char of the sequence,
    # prev_end should point to the last char
    # of the regular expression match.
    prev_end = m.end(0) - 1

if prev_end != (len(S) - 1):
    sub_strings.append(S[prev_end:len(S)])

# Key : length of sub string
# Value : number of sub string whose length matches the key.
dict = { }
count = len(S) # Count each char as 1.
for ss in sub_strings:
    if len(ss) in dict.keys():
        dict[len(ss)] += 1
    else:
        dict[len(ss)] = 1

keys = dict.keys()
for key in keys:
    if key == 2:
        # Consider the case when the two-length
        # strings appear in S many times.
        count += (dict[2] * 1)
    else:
        sum = 0
        for i in range(2, key + 1):
            sum += (key - i) + 1
        count += (sum * dict[key])

print(count % 998244353)
