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

# Calculate the minimum costs to move to the Nth room.
for idx in range(2, N):
    costs[idx] = min(costs[idx - 1] + A[idx - 1], costs[idx - 2] + B[idx - 2])
p(costs)

ans = []
idx = N - 1

while idx >= 0:
    ans.append(idx)
    # Which path A or B was chose ?
    #
    # This can be traced by checking the costs breakdown.
    # When the cur costs[idx] are made by previous costs
    # costs[idx - 1] and corresponding A[idx - 1]'s costs,
    # then it used A route. Otherwise, B route.
    if costs[idx] == costs[idx - 1] + A[idx - 1]:
        idx -= 1
    else:
        idx -= 2

print(len(ans))
print(*sorted([ n + 1 for n in ans ], reverse = False))
