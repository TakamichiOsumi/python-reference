#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

negative_counts = len(list(filter(lambda a:a < 0, A)))

positive_A = list(map(abs, A))
positive_A.sort(reverse = True)
if negative_counts % 2 == 0:
    print(sum(positive_A))
else:
    print(sum(positive_A[0:(N - 1)]) + (-1 *positive_A[-1]))
