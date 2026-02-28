#!/usr/bin/env python3

N = int(input())

decimal = []
octal = []

count = 0
for i in range(1, N + 1):
    if str(i).count('7') >= 1:
        decimal.append(i)
    if str(oct(i)).count('7') >= 1:
        octal.append(i)

octal.extend(decimal)
print(N - len(list(set(octal))))
