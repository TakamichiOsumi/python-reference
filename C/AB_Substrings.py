#!/usr/bin/env python3

import re

N = int(input())

XXXA = []
BXXX = []
BXXA = []
pair_count = 0
for i in range(N):
    s = input()

    pair_count = pair_count + len(re.findall('AB', s))
    if s[0] == 'B' and s[-1] == 'A':
        BXXA.append(s)
    elif s[0] == 'B':
        BXXX.append(s)
    elif s[-1] == 'A':
        XXXA.append(s)

# Possible extra pairs:
# 1. BXXA + BXXA
# 2. BXXA + BXXX
# 3. XXXA + BXXA
# 4. XXXA + BXXX
extra_pairs = 0

while len(BXXA) > 0:

    # Case 1
    if len(BXXA) >= 2 :
        tmp = BXXA.pop(0)
        tmp2 = BXXA.pop(0)
        extra_pairs = extra_pairs + 1
        # Created "BXXABXXA"
        BXXA.append(tmp + tmp2)
        continue

    # Case 3
    if len(XXXA) > 0:
        tmp = BXXA.pop(0)
        tmp2 = XXXA.pop(0)
        extra_pairs = extra_pairs + 1
        # Created "XXXABXXXA"
        XXXA.append(tmp2 + tmp)
        continue

    # Case 2
    if len(BXXX) > 0:
        tmp = BXXA.pop(0)
        tmp2 = BXXX.pop(0)
        extra_pairs = extra_pairs + 1
        # Created "BXXABXXX"
        BXXX.append(tmp + tmp2)
        continue

    # No pair can be created with BXXA now.
    break

# Add Case 4
print(pair_count + extra_pairs + min([len(XXXA), len(BXXX)]))
