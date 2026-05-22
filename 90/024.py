#!/usr/bin/env python3

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ary = [ abs(A[i] - B[i]) for i in range(N) ]

diff = sum(ary)
left = K - diff

# Can't make the same numbers.
if left < 0:
    print("No")
else:
    if left % 2 == 0:
        print("Yes")
    else:
        print("No")
