#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Don't forget the re-initialization logic.
#     In this problem, 'fac_N = start_N' is the
#     code for this.
# (2) SortedSet can be combined by union().

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
        # If fac_N is divided and there is
        # no remainder, then fac_N can be
        # divided by p.
        #
        # Continue this until any remainder
        # appears, which means no more division
        # can be conducted.
        #
        # Suppose a case p == 2 and fac_N is 120,
        # 120 => 60(0) => 30(0) => 15(0) => 7(1)
        # where the numbers in parenthesis are
        # remainders.
        while (fac_N % p) == 0:
            times += 1
            # Update the fac_N by the quotient,
            # only when remainder is zero.
            #
            # In the above example, replace 120
            # with 60.
            fac_N = fac_N // p
    multiple_counts.append(times + 1)

print(math.prod(multiple_counts) % (10 ** 9 + 7))
