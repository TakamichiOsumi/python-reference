#!/usr/bin/env python3

N = int(input())
S = [ input() for _ in range(N) ]

err = 0
logged_in = False
for s in S:

    if s == "login":
        logged_in = True
    elif s == "logout":
        logged_in = False
    elif s == "public":
        pass
    elif s == "private":
        if logged_in == False:
            err += 1

print(err)
