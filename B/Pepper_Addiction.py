#!/usr/bin/env python3

N, M = map(int, input().split())

C = list(map(int, input().split()))

total = 0
for i in range(N):
    A, B = map(int, input().split())

    A = A - 1
    left_gram = C[A]
    if left_gram >= B:
        left_gram = left_gram - B
        C[A] = left_gram
        total += B
        
    else:
        # B > left_gram
        consumption = C[A]
        C[A] = 0
        total += consumption

print(total)
