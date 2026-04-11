#!/usr/bin/env python3

N = int(input())
S = input()

idx = 0

if len(S) == S.count("o"):
    print("")
    exit()

while S[idx] == "o":
    S = S[1:len(S)]
print(S)
