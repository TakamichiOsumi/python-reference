#!/usr/bin/env python3

N = int(input())

ary = [0] * (N + 1)
ary[0] = 1
for i in range(N + 1):

    if i != 0:
        val = 0
        for j in range(i):
            val += sum(map(int, list(str(ary[j]))))
        ary[i] = val

print(ary[N])


