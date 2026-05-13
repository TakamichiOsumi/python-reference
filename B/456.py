#!/usr/bin/env python3

# Key Takeaways:
# (1) If the number of all of the combinations is small,
#     counting them and calculate the result might be fast to submit the answer.

import itertools

dices = [ list(map(int, input().split())) for _ in range(3) ]

patterns = list(itertools.product(dices[0], dices[1], dices[2]))

counts = 0
for p in patterns:
    l = list(p)
    if l.count(4) == 1 and l.count(5) and l.count(6):
        counts += 1

print((counts) / len(list(patterns)))
