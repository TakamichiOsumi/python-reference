#!/usr/bin/env python3

N = int(input())
S = list(input())

ans = 0
for i in range(N):
    c = S[i]
    if c == 'x':
        if i == 0 or S[i - 1] == 'x':
            if i == (N - 1) or S[i + 1] == 'x':
                ans += 1
print(ans)
