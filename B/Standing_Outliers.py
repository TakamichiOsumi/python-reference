#!/usr/bin/env python3

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = []
for i in range(N):
    con = True
    for j in range(N):
        target = X[i]
        if j == i:
            continue
        else:
            p("i=", i, ", j=", j, ":",X[i],X[j], "=>", abs(X[i] - X[j]))
            if abs(X[i] - X[j]) >= D:
                pass
            else:
                con = False
    if con:
        ans.append(i + 1)

print(len(ans))
print(*sorted(ans, reverse = False))
