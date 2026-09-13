#!/usr/bin/env python3

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

S = list(input())
print("o".join(S))
