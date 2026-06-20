#!/usr/bin/env python3

# This won't be accepted as AC.
# Debugging is in progress.

N, M = map(int, input().split())

zero = False
duplicate = False
digits_and_val = {}

for i in range(M):
    s, c = map(int, input().split())
    
    if s in digits_and_val.keys():
        if digits_and_val[s] != c:
            duplicate = True
    else:
        digits_and_val[s] = c
        if s == 1 and c == 0:
            zero = True

if duplicate:
    print(-1)
    exit()

if zero == True and N >= 2:
    print(-1)
    exit()

min_val = 1000
digits = set(digits_and_val.keys())
for i in range(1000):
    satisfied_count = 0
    
    str_i = str(i)
    if len(str_i) >= 3 and (3 in digits) and digits_and_val[3] == int(str_i[2]):
        satisfied_count += 1

    if len(str_i) >= 2 and (2 in digits) and digits_and_val[2] == int(str_i[1]):
        satisfied_count += 1

    if len(str_i) >= 1 and (1 in digits) and digits_and_val[1] == int(str_i[0]):
        satisfied_count += 1

    if satisfied_count == len(digits):
        min_val = min(min_val, i)
        break

print(min_val)
