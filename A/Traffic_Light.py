#!/usr/bin/env python3

main = "BYR"
S = input()
print(main[(main.index(S) + 1) % 3])
