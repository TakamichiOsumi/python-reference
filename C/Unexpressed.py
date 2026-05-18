#!/usr/bin/env python3

N = int(input())

count = 0

s = set([])

ignore_rest = False
for i in range(2, N + 1):
    for j in range(2, N + 1):
        val = i ** j
        if val<= N:
            count += 1
            s.add(val)
        else:
            if j == 2:
                ignore_rest = True
            break

    if ignore_rest:
        break

print(N - len(s))
