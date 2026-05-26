#!/usr/bin/env python3

# Key Takeaways:

# Get used to np.base_repr(N, M) and int(N, M).
# String 'N' is interpreted as M-adic, when 'N' is passed to int(N, M)
# np.base_repr(N, M) converts N to a number of 'M' base representation.

import numpy as np

N, K = input().split()

N = int(N, 8)
K = int(K)
for _ in range(K):
    N = np.base_repr(N, 9)
    sN = str(N)
    N = int(sN.replace("8", "5"), 8)

print(np.base_repr(N, 8))

