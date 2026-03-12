#!/usr/bin/env python3

X, K, D = map(int, input().split())

if X > 0:
    if X - (K * D) > 0:
        print(X - (K * D))
    elif X  - (K * D) < 0:
        used = (X // D) + 1
        if (K - used) % 2 == 0:
            print(abs(X - used * D))
        else:
            print(abs(X - (used * D) + D))
    else:
        # X - (K * D) == 0:
        print(0)
elif X < 0:
    if X + (K * D) < 0:
        print(abs(X + (K * D)))
    elif X + (K * D) > 0:
        used = (abs(X) // D) + 1
        if (K - used) % 2 == 0:
            print(abs(X + used * D))
        else:
            print(abs(X + (used * D) - D))
    else:
        # X + (K * D) == 0:
        print(0)
else:
    # X == 0
    if K % 2 == 0:
        print(0)
    else:
        print(D)
