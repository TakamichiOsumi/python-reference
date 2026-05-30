#!/usr/bin/env python3

T = input()
U = input()

for i in range(len(T) - len(U) + 1):
    sub = T[i:(i + len(U))]
    found = True
    for j in range(len(sub)):
        if sub[j] == '?':
            pass
        else:
            if sub[j] == U[j]:
                pass
            else:
                found = False
    if found:
        break

if found:
    print("Yes")
else:
    print("No")
