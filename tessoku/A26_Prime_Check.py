#!/usr/bin/env python3

from sortedcontainers import SortedSet
from collections import defaultdict

debug = True # switch
def p(*var):
    global debug
    if debug:
        if len(var) == 1 and type(var[0]) == type([]):
            print("DEBUG : --argument array--")
            for i in range(len(var[0])):
                print(f"\t{i}:{var[0][i]}")
        else:
            print("DEBUG:", *var)


def is_prime(val):
    i = 2
    while True:
        if i * i > val:
            break
        if val % i == 0:
            return False
        i += 1
        if i == val:
            break
    return True

Q = int(input())

primes = SortedSet([])

for i in range(Q):
    x = int(input())
    if x in primes or is_prime(x):
        primes.add(is_prime(x))
        print("Yes")
    else:
        print("No")
