#!/usr/bin/env python3

N, K = map(int, input().split())

x = N
for k in range(K):

    g1 = sorted(list(str(x)), reverse = True)
    g2 = sorted(list(str(x)), reverse = False)
    # print("g1 =", g1, ", g2 =", g2)

    x = int("".join(g1)) - int("".join(g2))

print(x)
