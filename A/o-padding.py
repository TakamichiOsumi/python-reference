#!/usr/bin/env python3

debug_mode = False
def p(var):
    global debug_mode
    if debug_mode:
        print("DEBUG:", var)

N = int(input())
S = input()

p(N)
p(S)

print("".join(['o' * (N - len(S))]) + S)
