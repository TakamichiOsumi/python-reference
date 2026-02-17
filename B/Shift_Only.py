#!/usr/bin/env python3

N = int(input())
ary = list(map(int, input().split()))

count = 0
while(True):

    half = [n % 2 for n in ary]
    if (int(sum(half)) == 0):
        count = count + 1
        ary = [ int(n / 2) for n in ary]
    else:
        break

print(count)
