#!/usr/bin/env python3

from sortedcontainers import SortedSet
import math

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

N = int(input())
primes_set = SortedSet()
for i in range(2, N + 1):
    new_set = prime_factorization(i)
    primes_set = primes_set.union(new_set)

start_N = math.factorial(N)
multiple_counts = []
for p in primes_set:
    times = 0

    if p == N:
        times = 1
    else:
        fac_N = start_N
        while (fac_N % p) == 0:
            times += 1
            fac_N = fac_N // p
    multiple_counts.append(times + 1)

print(math.prod(multiple_counts) % (10 ** 9 + 7))

