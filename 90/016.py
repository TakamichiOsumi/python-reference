#!/usr/bin/env python3

N = int(input())
Num = list(map(int, input().split()))
sorted_Num = sorted(Num, reverse = True)
A = sorted_Num[0]
B = sorted_Num[1]
C = sorted_Num[2]
min_val = 10000
for i in range(10000):
    for j in range(10000):
        left = N - (i * A + j * B)
        if left % C == 0 and left >= 0:
            if (i + j + (left // C)) <= 9999:
                min_val = min(i + j + (left // C), min_val)
print(min_val)
