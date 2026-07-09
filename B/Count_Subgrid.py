#!/usr/bin/env python3

# Key Takeaways:
#
# (1) Nesting a smaller matrix in another matrix
#     can be done based on an idea that the size
#     of M - 1 cannot be used at the right and
#     the bottom edge. Then, loop times is
#     'N - (M - 1)'. The -1 is the used cell in
#     the inner matrix.
#
# (2) Tuple can't be updated since it's immutable.
#     Apply set() to tuple converted from list to
#     filter unique combinations.

N, M = map(int, input().split())

S = [ list(input()) for _ in range(N) ]

if N == M:
    print(1)
    exit()

pairs = []
for i in range(N - (M - 1)):
    for j in range(N - (M - 1)):
        l = []
        for ver in range(M):
            for hori in range(M):
                l.append(S[i + ver][j + hori])

        pairs.append(tuple(l))

print(len(set(pairs)))

