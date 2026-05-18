#!/usr/bin/env python3

S = input()
T = input()

chars = [chr(i) for i in range(97, 97+26)]

if S == T[0:len(T) - 1]:
    if T[len(T) - 1] in chars:
        print("Yes")
    else:
        print("No")
else:
    print("No")
