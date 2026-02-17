#!/usr/bin/env python3

N = input()

words = []
idx = 0
while True:

    # This idx must be the first character of one word.
    left = idx
    right = idx + 1
    while N[right].islower():
        right = right + 1
    
    # Found a word made more than 3 chars.
    words.append(N[left:right + 1])
    idx = right + 1
    if idx >= len(N):
        break

print("".join(sorted(words, key = str.lower)))
