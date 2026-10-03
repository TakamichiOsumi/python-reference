#!/usr/bin/env python3

debug = True # switch
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

costs = [10 ** 9] * N
costs[0] = 0
costs[1] = A[0]

p(costs)

for i in range(2, N):
    c1 = costs[i - 1] + A[i - 1]
    c2 = costs[i - 2] + B[i - 2]
    if c1 <= c2:
        costs[i] = c1
    else:
        costs[i] = c2
p(costs)

print(costs[N - 1])
