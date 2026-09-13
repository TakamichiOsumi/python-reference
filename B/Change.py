#!/usr/bin/env python3

debug = False
def p(*var):
    global debug
    if debug:
        print("DEBUG:", *var)

N = int(input())
A = list(map(int, input().split()))

one = 0
ten = 0
hundred = 0

for i in range(len(A)):

    val = A[i]
    pay = 0
    while True:

        if (pay * 1000) >= val:
            break
        else:
            pay += 1

    diff = pay * 1000 - val
    diff = str(diff).zfill(3)
    digits = list(map(int, list(str(diff))))
    hundred += digits[0]
    ten += digits[1]
    one += digits[2]

print(one, ten, hundred)
