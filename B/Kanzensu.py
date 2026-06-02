#!/usr/bin/env python3

from sortedcontainers import SortedSet

N = int(input())

def get_divisors(N, include_edges = True, include_pair = True):
    if include_edges:
        div = SortedSet([1, N])
    else:
        div = SortedSet([])
    i = 2
    while True:
        if i * i > N:
            break
        if N % i == 0:
            div.add(i)
            if include_pair and N // i != i:
                div.add(N // i)
        i += 1
    return div

div = get_divisors(N,
                   include_edges = False,
                   include_pair = True)

# Exclude adding 1 when N == 1,
# since sum of perfect number
# should remove N itself.
if 2 <= N:
    div.add(1)

value = sum(list(div))

if value == N:
    print("Perfect")
elif value < N:
    print("Deficient")
else:
    print("Abundant")
