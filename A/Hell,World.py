#!/usr/bin/env python3

S = list("HelloWorld")
S.pop(int(input()) - 1)
S = "".join(S)
print(S)
