#!/usr/bin/env python3

import numpy as np

N, K = input().split()

N = int(N, 8)
K = int(K)
for _ in range(K):
    N = np.base_repr(N, 9)
    sN = str(N)
    N = int(sN.replace("8", "5"), 8)

print(np.base_repr(N, 8))

