#!/usr/bin/env python3

def get_divisors(N):
    i = 2
    last_pairs = []
    while True:
        if i * i > N:
            break
        if N % i == 0:
            last_pairs = [i, N // i]
        i += 1
    return last_pairs

N = int(input())
l = list(get_divisors(N))
if len(l) == 0:
    print(len(str(N)))
else:
    sl = list(map(str, l))
    digits = [ len(sl[i]) for i in range(len(sl)) ]
    print(max(digits))
