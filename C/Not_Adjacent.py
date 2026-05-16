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

# If m.end(0) didn't reach the end of 'S',
# add the last substring based on prev_end.
if prev_end != (len(S) - 1):
    sub_strings.append(S[prev_end:len(S)])

count = len(S)
for s in sub_strings:
    count += (len(s) * (len(s) - 1) / 2)
print(int(count % 998244353))
