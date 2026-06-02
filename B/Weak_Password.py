#!/usr/bin/env python3

S = input()

if S[0] == S[1] == S[2] == S[3]:
    print("Weak")
else:
    cond1 = ((int(S[0]) + 1) % 10) == int(S[1])
    cond2 = ((int(S[1]) + 1) % 10) == int(S[2])
    cond3 = ((int(S[2]) + 1) % 10) == int(S[3])
    if cond1 and cond2 and cond3:
        print("Weak")
    else:
        print("Strong")
