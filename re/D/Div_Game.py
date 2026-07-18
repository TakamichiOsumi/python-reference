#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Reuse the reference function and save the time.
#
# (2) If 'i' is set to large enough and the division of 'N / (p ** i)'
#     is repeatedly executed, having 'break' in the middle of the loop
#     works to find the biggeest 'i' during the loop. In this example,
#     the end limit for 'i' is set to '10 ** 6'.

from sortedcontainers import SortedList, SortedDict, SortedSet
import math

N = int(input())

def prime_factorization(orig_N):
    N = orig_N
    factors = []
    i = 2
    while True:
        if i * i > orig_N:
            break
        if N % i == 0:
            while N % i == 0:
                factors.append(i)
                N = N // i
        i += 1

    if N != 1:
        factors.append(N)

    return factors


if N == 1:
    print(0)
    exit()

ssp = SortedSet(prime_factorization(N))

ans = 0
for p in ssp:
    for i in range(1, 10 ** 6):
        if N % (p ** i) == 0:
            N = N / (p ** i)
            ans += 1
        else:
            break

print(ans)

