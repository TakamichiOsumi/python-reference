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
    
    words.append(N[left:right + 1])
    idx = right + 1
    if idx >= len(N):
        break

# The str.lower key is required. Without the key,
# the sort results are affected by lower and upper letters.
print("".join(sorted(words, key = str.lower)))
