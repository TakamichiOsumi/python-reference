#!/bin/python

S = input()

cond = True
c_count = 0
for i in range(0, len(S)):
    if i == 0:
        if S[i] != "A":
            cond = False
    elif 2 <= i <= len(S) - 2:
        if S[i] == "C":
            c_count = c_count + 1
    else:
        if S[i].islower() == False:
            cond = False

if cond == False:
    print("WA")
else:
    if c_count == 1:
        print("AC")
    else:
        print("WA")
