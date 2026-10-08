#!/usr/bin/env python3

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

S = int(input())
dp = [0] * (S + 1)

for i in range(3, S + 1):
    dp[i] = (sum(dp[3:i - 2]) + 1) % (10 ** 9 + 7)

print(dp[S])
