#!/usr/bin/env python3

N, X = input().split()

if X == "A":
    idx = 0
elif X == "B":
    idx = 1
elif X == "C":
    idx = 2
elif X == "D":
    idx = 3
elif X == "E":
    idx = 4

ans = False
found = False
for _ in range(int(N)):
    s = input()
    seats = list(s)
    if found:
        continue
    if seats[idx] == 'o':
        found = ans = True

if ans:
    print("Yes")
else:
    print("No")
    
